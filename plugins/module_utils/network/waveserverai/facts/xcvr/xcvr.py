#
# -*- coding: utf-8 -*-
# Copyright 2021 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The waveserverai xcvr fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from copy import deepcopy

from ansible.module_utils._text import to_bytes
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)

from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.argspec.xcvr.xcvr import (
    XcvrArgs,
)
from ansible.module_utils.six import string_types

try:
    from lxml import etree

    HAS_LXML = True
except ImportError:
    HAS_LXML = False


class XcvrFacts(object):
    """The waveserverai xcvr fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = XcvrArgs.argument_spec
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
        """Populate the facts for xcvr
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        if not HAS_LXML:
            self._module.fail_json(msg="lxml is not installed.")

        if not data:
            raise Exception("Not yet Implemented")
        if isinstance(data, string_types):
            data = etree.fromstring(
                to_bytes(data, errors="surrogate_then_replace")
            )

        resources = data.xpath("configuration/xcvr")

        objs = []
        for resource in resources:
            if resource:
                obj = self.render_config(self.generated_spec, resource)
                if obj:
                    objs.append(obj)

        facts = {}
        if objs:
            facts["resource"] = []
            params = utils.validate_config(
                self.argument_spec, {"config": objs}
            )
            for cfg in params["config"]:
                facts["resource"].append(utils.remove_empties(cfg))

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
        config["name"] = utils.get_xml_conf_arg(conf, "name")
        config["some_value"] = utils.get_xml_conf_arg(conf, "some_value")
        return utils.remove_empties(config)

    def get(self, filter=None, with_defaults=None):
        """
        Retrieve device configuration and state information.
        :param filter: This argument specifies the portion of the state data to retrieve
                       (by default entire state data is retrieved)
        :param with_defaults: defines an explicit method of retrieving default values
                              from the configuration
        :return: Returns xml string containing the RPC response received from remote host
        """
        if isinstance(filter, list):
            filter = tuple(filter)
        resp = self.m.get(filter=filter, with_defaults=with_defaults)
        response = resp.data_xml if hasattr(resp, "data_xml") else resp.xml
        return response
