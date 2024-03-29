#
# -*- coding: utf-8 -*-
# Copyright 2021 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The waveserverai xcvrs fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from copy import deepcopy
from ansible.module_utils._text import to_text, to_bytes
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.netconf.netconf import (
    get,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    remove_namespaces,
)
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.argspec.xcvrs.xcvrs import (
    XcvrsArgs,
)
try:
    from lxml.etree import tostring as xml_to_string, fromstring

    HAS_LXML = True
except ImportError:
    from xml.etree.ElementTree import fromstring, tostring as xml_to_string

    HAS_LXML = False


class XcvrsFacts(object):
    """The waveserverai xcvrs fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = XcvrsArgs.argument_spec
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
        """Populate the facts for xcvrs
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            config_filter = """
                <xcvr:waveserver-xcvrs xmlns:xcvr="urn:ciena:params:xml:ns:yang:ciena-ws:ciena-waveserver-xcvr">
                    <xcvr:xcvrs>
                        <xcvr:state/>
                    </xcvr:xcvrs>
                </xcvr:waveserver-xcvrs>
                """
            data = get(self._module, filter=("subtree", config_filter))

        stripped = remove_namespaces(xml_to_string(data))
        data = fromstring(to_bytes(stripped, errors="surrogate_then_replace"))

        resources = data.xpath("/data/waveserver-xcvrs/xcvrs")

        objs = []
        for resource in resources:
            if resource:
                obj = self.render_config(self.generated_spec, resource)
                if obj:
                    objs.append(obj)
        facts = {}
        if objs:
            facts["xcvrs"] = []
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )
            for cfg in params["config"]:
                facts["xcvrs"].append(utils.remove_empties(cfg))

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts

    def render_config(self, spec, conf):
        """
        Render config as dictionary structure and delete keys
          from spec for null values

        :param spec: The facts tree, generated from the argspec
        :param conf: The configuration
        :rtype: dictionary
        :returns: The generated config
        """
        config = deepcopy(spec)
        config["xcvr-id"] = utils.get_xml_conf_arg(conf, "xcvr-id")
        config["properties"]["mode"] = utils.get_xml_conf_arg(
            conf, "state/actual-mode"
        )
        return utils.remove_empties(config)
