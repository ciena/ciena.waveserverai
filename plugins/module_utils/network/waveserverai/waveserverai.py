# (c) 2021 Ciena Corp.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type
import json

from ansible.module_utils._text import to_text, to_bytes
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    NetconfConnection,
    remove_namespaces,
)

try:
    from lxml.etree import tostring as xml_to_string, fromstring

    HAS_LXML = True
except ImportError:
    from xml.etree.ElementTree import fromstring, tostring as xml_to_string

    HAS_LXML = False

_DEVICE_CONFIGS = {}
CONFIG_FORMATS = frozenset(["xml", "text", "json", "set"])

waveserverai_provider_spec = {
    "host": dict(),
    "port": dict(type="int"),
    "username": dict(fallback=(env_fallback, ["ANSIBLE_NET_USERNAME"])),
    "password": dict(fallback=(env_fallback, ["ANSIBLE_NET_PASSWORD"]), no_log=True),
    "ssh_keyfile": dict(fallback=(env_fallback, ["ANSIBLE_NET_SSH_KEYFILE"]), type="path"),
    "timeout": dict(type="int"),
    "transport": dict(default="netconf", choices=["cli", "netconf"]),
}
waveserverai_argument_spec = {
    "provider": dict(
        type="dict",
        options=waveserverai_provider_spec,
        removed_at_date="2022-06-01",
        removed_from_collection="ciena.waveserverai",
    )
}


def remove_ns(element):
    data = remove_namespaces(xml_to_string(element))
    root = fromstring(to_bytes(data, errors="surrogate_then_replace"))
    return root


def tostring(element, encoding="UTF-8"):
    if HAS_LXML:
        return xml_to_string(element, encoding="unicode")
    else:
        return to_text(xml_to_string(element, encoding), encoding=encoding)


def get_provider_argspec():
    return waveserverai_provider_spec


def get_connection(module):
    if hasattr(module, "_waveserverai_connection"):
        return module._waveserverai_connection

    capabilities = get_capabilities(module)
    network_api = capabilities.get("network_api")
    if network_api == "cliconf":
        module._waveserverai_connection = Connection(module._socket_path)
    elif network_api == "netconf":
        module._waveserverai_connection = NetconfConnection(module._socket_path)
    else:
        module.fail_json(msg="Invalid connection type %s" % network_api)

    return module._waveserverai_connection


def get_capabilities(module):
    if hasattr(module, "_waveserverai_capabilities"):
        return module._waveserverai_capabilities

    try:
        capabilities = Connection(module._socket_path).get_capabilities()
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))

    module._waveserverai_capabilities = json.loads(capabilities)
    return module._waveserverai_capabilities


def get_configuration(module, source="running", format="xml", filter=None):
    if format not in CONFIG_FORMATS:
        module.fail_json(msg="invalid config format specified")

    conn = get_connection(module)
    try:
        reply = conn.get_config(source=source)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    return reply


def run_commands(module, commands, check_rc=True):
    """Send a list of commands to the device over the active connection."""

    capabilities = get_capabilities(module)
    network_api = capabilities.get("network_api")
    if network_api != "cliconf":
        module.fail_json(
            msg=(
                "waveserverai_command requires ansible_connection=network_cli. "
                "Current connection type is '%s'." % (network_api or "unknown")
            )
        )

    connection = get_connection(module)
    try:
        response = connection.run_commands(commands=commands, check_rc=check_rc)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    return response
