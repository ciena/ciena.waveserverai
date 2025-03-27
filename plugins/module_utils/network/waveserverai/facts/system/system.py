#
# -*- coding: utf-8 -*-
# Copyright 2025 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The waveserverai system fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


from copy import deepcopy

import re  # pylint: disable=unused-import
from ansible.module_utils._text import to_bytes
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    remove_namespaces,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.netconf.netconf import (
    get,
)
from ansible_collections.ciena.system.plugins.module_utils.network.waveserverai.argspec.system.system import (
    SystemArgs,
)

try:
    from lxml.etree import tostring as xml_to_string, fromstring

    HAS_LXML = True
except ImportError:
    from xml.etree.ElementTree import tostring as xml_to_string, fromstring

    HAS_LXML = False


class SystemFacts(object):
    """The waveserverai system fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = SystemArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for system
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            config_filter = """
                <waveserver-system xmlns="urn:ciena:params:xml:ns:yang:ciena-ws:ciena-waveserver-system">
                </waveserver-system>
                """
            data = get(self._module, filter=("subtree", config_filter))

        stripped = remove_namespaces(xml_to_string(data))
        data = fromstring(to_bytes(stripped, errors="surrogate_then_replace"))

        resource = data.xpath("/rpc-reply/data/waveserver-system")[0]
        obj = self.render_config(self.generated_spec, resource)

        facts = {}
        facts["system"] = {}
        params = utils.validate_config(self.argument_spec, {"config": obj})
        facts["system"] = params["config"]

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def get_xml_value(self, xml_obj, xpath):
        result = xml_obj.xpath(xpath)
        return result[0].text if result else None

    def recursive_config_fill(self, config, conf, spec, xml_base_path=""):
        for key, unused in spec.items():
            modified_key = key.replace("_", "-")
            new_base_path = f"{xml_base_path}/{modified_key}" if xml_base_path else modified_key

            if isinstance(spec[key], dict):
                config[key] = {}
                self.recursive_config_fill(config[key], conf, spec[key], new_base_path)
            else:
                extracted_value = self.get_xml_value(conf, new_base_path)
                if extracted_value is not None:
                    config[key] = extracted_value

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        if isinstance(conf, str):
            conf = fromstring(conf)
        config = {}
        self.recursive_config_fill(config, conf, spec)
        return utils.remove_empties(config)
