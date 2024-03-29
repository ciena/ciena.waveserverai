#
# -*- coding: utf-8 -*-
# Copyright 2021 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The waveserverai_xcvrs class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible.module_utils._text import to_text, to_bytes

from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.waveserverai import (
    xml_to_string,
    fromstring,
)

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_list,
)
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.facts.facts import (
    Facts,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    remove_namespaces,
    build_root_xml_node,
    build_child_xml_node,
)

from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.utils.utils import (
    config_is_diff
)


class Xcvrs(ConfigBase):
    """
    The waveserverai_xcvrs class
    """

    gather_subset = ['!all', '!min']
    gather_network_resources = ['xcvrs']

    def __init__(self, module):
        super(Xcvrs, self).__init__(module)

    def get_xcvrs_facts(self):
        """ Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset, self.gather_network_resources
        )
        xcvrs_facts = facts['ansible_network_resources'].get('xcvrs')
        if not xcvrs_facts:
            return []
        return xcvrs_facts

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {'changed': False}
        existing_xcvrs_facts = self.get_xcvrs_facts()
        config_xmls = self.set_config(existing_xcvrs_facts)

        for config_xml in to_list(config_xmls):
            config = f'<config>{config_xml.decode("utf-8")}</config>'
            kwargs = {
                "config": config,
                "target": "running",
                "default_operation": "merge",
                "format": "xml",
            }

            self._module._connection.edit_config(**kwargs)
        result["xml"] = config_xmls
        changed_xcvrs_facts = self.get_xcvrs_facts()

        result["changed"] = not config_is_diff(existing_xcvrs_facts, changed_xcvrs_facts)

        result["before"] = existing_xcvrs_facts
        if result["changed"]:
            result["after"] = changed_xcvrs_facts

        return result

    def set_config(self, existing_xcvrs_facts):
        """ Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params['config']
        have = existing_xcvrs_facts
        resp = self.set_state(want, have)
        return to_list(resp)

    def set_state(self, want, have):
        """ Select the appropriate function based on the state provided

        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        root = build_root_xml_node("waveserver-xcvrs")
        state = self._module.params["state"]
        if state == "overridden":
            config_xmls = self._state_overridden(want, have)
        elif state == 'deleted':
            config_xmls = self._state_deleted(want, have)
        elif state == 'merged':
            config_xmls = self._state_merged(want, have)
        elif state == 'replaced':
            config_xmls = self._state_replaced(want, have)

        for xml in config_xmls:
            root.append(xml)
        data = remove_namespaces(xml_to_string(root))
        root = fromstring(to_bytes(data, errors="surrogate_then_replace"))

        return xml_to_string(root)

    def _state_replaced(self, want, have):
        """ The command generator when state is replaced

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml

    def _state_overridden(self, want, have):
        """ The command generator when state is overridden

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml

    def _state_deleted(self, want, have):
        """ The command generator when state is deleted

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        intf_xml = []
        return intf_xml

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the xml necessary to migrate the current configuration
                  to the desired configuration
        """
        xcvrs_xml = []
        for child in want:
            xcvrs_root = build_root_xml_node("xcvrs")
            xcvrs = build_child_xml_node(xcvrs_root, "xcvrs")
            build_child_xml_node(xcvrs, "xcvr-id", child["xcvr-id"])
            properties = build_child_xml_node(xcvrs, "properties")
            build_child_xml_node(
                properties, "mode", child["properties"]["mode"]
            )
            xcvrs_xml.append(xcvrs)
        return xcvrs_xml
