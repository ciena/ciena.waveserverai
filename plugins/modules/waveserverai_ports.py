#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2025 Ciena
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for waveserverai_ports
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
---
module: waveserverai_ports
short_description: Waveserver port configuration and operational data.Manage the ports ports configuration of a Ciena waveserverai device
description: "Waveserver port configuration and operational data.\n Configuration and operational data for the port."
author: Ciena
options:
  config:
    description: Configuration and operational data for the port.
    type: list
    elements: dict
    suboptions:
      channels:
        description: List of ODU4 channels within the parent OTU port object.
        type: list
        elements: dict
        suboptions:
          channel_id:
            description: 'Channel number or ODU4 tributary number within the parent OTU port object. Key value for the channels list. (Key for
              list: channels)'
            type: int
            required: true
          id:
            description: Channel identification attributes.
            type: dict
            suboptions:
              label:
                description: The user-specified label string for this channel object.
                type: str
                required: false
          properties:
            description: Channel properties.
            type: dict
            suboptions:
              odu_sd_threshold:
                description: ODU4 Signal Degrade threshold value.
                type: str
                required: false
              trace:
                description: ODU4 path trace attributes for this channel.
                type: dict
                suboptions:
                  exp_dapi:
                    description: The expected destination access point identifier (DAPI) portion of the received trace string, up to 15 characters,
                      excluding the first byte in the TTI DAPI overhead, which is implicitly always null.
                    type: str
                    required: false
                  exp_oper:
                    description: The expected operator-specific portion of the received trace string, up to 32 characters.
                    type: str
                    required: false
                  exp_sapi:
                    description: The expected source access point identifier (SAPI) portion of the received trace string, up to 15 characters,
                      excluding the first byte in the TTI SAPI overhead, which is implicitly always null.
                    type: str
                    required: false
                  mismatch_fail_mode:
                    description: The trail trace identifier (TTI) mismatch failure mode. When TTI mismatch condition occurs, this indicates the
                      consequent action taken, e.g. whether or not to raise an alarm.
                    type: str
                    required: false
                    choices:
                    - none
                    - alarm-only
                    - squelch-traffic
                  mismatch_mode:
                    description: The trail trace identifier (TTI) mismatch mode, indicating which fields of the TTI overhead are used for trace
                      mismatch detection.
                    type: str
                    required: false
                    choices:
                    - operator-only
                    - sapi
                    - dapi
                    - sapi-and-dapi
                  tx_dapi:
                    description: The destination access point identifier (DAPI) portion of the transmitted trace string, up to 15 characters,
                      excluding the first byte in the TTI DAPI overhead, which is implicitly always null.
                    type: str
                    required: false
                  tx_oper:
                    description: The operator-specific portion of the transmitted trace string, up to 32 characters. Ignored if tx-oper-mode is
                      'automatic'.
                    type: str
                    required: false
                  tx_oper_mode:
                    description: Specifies whether to allow manual provisioning of the transmitted TTI string, or let the system assign this value
                      automatically based on a pre-defined format.
                    type: str
                    required: false
                    choices:
                    - manual
                    - automatic
                  tx_sapi:
                    description: The source access point identifier (SAPI) portion of the transmitted trace string, up to 15 characters, excluding
                      the first byte in the TTI SAPI overhead, which is implicitly always null.
                    type: str
                    required: false
          state:
            description: Channel administrative and operational states.
            type: dict
            suboptions:
              admin_state:
                description: The configured administrative state of the channel.
                type: str
                required: false
                choices:
                - disabled
                - enabled
        key: channel-id
      id:
        description: Port identification attributes.
        type: dict
        suboptions:
          type:
            description: The port interface type.
            type: str
            required: false
            choices:
            - unknown
            - ethernet
            - otn
            - OTUk
            - OTUCn
            - OTUCn-Flex
            - ET
          label:
            description: The user-specified label string for this port interface.
            type: str
            required: false
      port_id:
        description: 'Unique, access identifier string of the port in ''<slot>-<port>'' format. (Key for list: ports)'
        type: str
        required: true
      properties:
        description: Port properties.
        type: dict
        suboptions:
          connection_peer:
            description: Port connection peer list. Indicates the client/line port/channel that may be connected to this line/client port. For
              certain client ports, the connection state is user-configurable or can be system assigned on port creation based on bandwidth availability.
              For other ports, the connection state is fixed and cannot be manually configured.
            type: list
            elements: dict
            suboptions:
              peer_id:
                description: 'Specifies the client/line connection information for the port or channel. Client ports can be connected to a line-side
                  channel or port. Line ports can be connected to a client side port. Line channels can be connected to one or more client ports.
                  The connection mappings are static and provided by the system based on XCVR configuration. (Key for list: connection-peer)'
                type: str
                required: true
            key: peer-id
          connection_state:
            description: Specifies whether the line-side bandwidth is allocated for the connection between this client port and its connection
              peer. For most client port types, this is enabled by default and cannot be disabled. For certain client ports that can share line-side
              bandwidth with other client ports (such as on MOTR-AGG modules), the connection state can be manually configured by the user in
              order to assign or release the line-side bandwidth to the desired client. On the line-side, the connection state is read-only.
            type: str
            required: false
            choices:
            - disabled
            - enabled
          ethernet:
            description: Ethernet-specific properties.
            type: dict
            suboptions:
              conditioning_holdoff:
                description: Number of milliseconds to delay Egress UNI port consequent action for an EPL service.
                type: int
                required: false
              conditioning_type:
                description: Egress UNI port consequent action for an EPL service to be applied on a far-end ingress UNI failure or network failure.
                  Supported values are 'none', 'laser-off', and 'ethernet'.
                type: str
                required: false
                choices:
                - none
                - laser-off
                - ethernet
                - otn
                - protocol-specific
          loopback:
            description: Port PHY layer loopback. RX loopback is a loopback forwarding ingress traffic from RX port directly to TX port. TX loopback
              is a loopback forwarding egress traffic from TX port directly to RX port, TX loopback is not supported in I-NNI ports. The RX/TX
              loopback can only be enabled when the port admin-state is disabled. Enable an RX/TX loopback shall fail when the port has its admin-state
              enabled. Users shall be able to disable the xcvr/ptp when its child port loopback enabled. Enable xcvr/ptp shall not enable its
              child port with loopback enabled. A port shall has its operational state rx loopback when rx loopback is enabled, and tx loopback
              when tx loopback is enabled.
            type: str
            required: false
            choices:
            - disabled
            - rx
            - tx
          otn:
            description: OTN-specific properties.
            type: dict
            suboptions:
              conditioning_type:
                description: Conditioning type for OTN ports. Supported values are 'laser-off' and 'otn'.
                type: str
                required: false
                choices:
                - none
                - laser-off
                - ethernet
                - otn
                - protocol-specific
              odu_sd_threshold:
                description: ODUk Signal Degrade threshold value, e.g. '1E-05' to '1E-09'.
                type: str
                required: false
              odu_termination:
                description: ODUk termination mode.
                type: str
                required: false
                choices:
                - terminated
                - passthrough
              otu_sd_threshold:
                description: OTU Signal Degrade threshold value, e.g. '1E-06' to '1E-09'.
                type: str
                required: false
              overhead_aggregation_mode:
                description: Overhead aggregation mode.
                type: str
                required: false
                choices:
                - single-slice
                - automatic
              trace:
                description: OTN port trace attributes
                type: dict
                suboptions:
                  path:
                    description: ODUk path trace attributes for this port.
                    type: dict
                    suboptions:
                      exp_dapi:
                        description: The expected destination access point identifier (DAPI) portion of the received trace string, up to 15 characters,
                          excluding the first byte in the TTI DAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                      exp_oper:
                        description: The expected operator-specific portion of the received trace string, up to 32 characters.
                        type: str
                        required: false
                      exp_sapi:
                        description: The expected source access point identifier (SAPI) portion of the received trace string, up to 15 characters,
                          excluding the first byte in the TTI SAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                      mismatch_fail_mode:
                        description: The trail trace identifier (TTI) mismatch failure mode. When TTI mismatch condition occurs, this indicates
                          the consequent action taken, e.g. whether or not to raise an alarm.
                        type: str
                        required: false
                        choices:
                        - none
                        - alarm-only
                        - squelch-traffic
                      mismatch_mode:
                        description: The trail trace identifier (TTI) mismatch mode, indicating which fields of the TTI overhead are used for
                          trace mismatch detection.
                        type: str
                        required: false
                        choices:
                        - operator-only
                        - sapi
                        - dapi
                        - sapi-and-dapi
                      tx_dapi:
                        description: The destination access point identifier (DAPI) portion of the transmitted trace string, up to 15 characters,
                          excluding the first byte in the TTI DAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                      tx_oper:
                        description: The operator-specific portion of the transmitted trace string, up to 32 characters. Ignored if tx-oper-mode
                          is 'automatic'.
                        type: str
                        required: false
                      tx_oper_mode:
                        description: Specifies whether to allow manual provisioning of the transmitted TTI string, or let the system assign this
                          value automatically based on a pre-defined format.
                        type: str
                        required: false
                        choices:
                        - manual
                        - automatic
                      tx_sapi:
                        description: The source access point identifier (SAPI) portion of the transmitted trace string, up to 15 characters, excluding
                          the first byte in the TTI SAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                  section:
                    description: OTUk section trace attributes for this port.
                    type: dict
                    suboptions:
                      exp_dapi:
                        description: The expected destination access point identifier (DAPI) portion of the received trace string, up to 15 characters,
                          excluding the first byte in the TTI DAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                      exp_oper:
                        description: The expected operator-specific portion of the received trace string, up to 32 characters.
                        type: str
                        required: false
                      exp_sapi:
                        description: The expected source access point identifier (SAPI) portion of the received trace string, up to 15 characters,
                          excluding the first byte in the TTI SAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                      mismatch_fail_mode:
                        description: The trail trace identifier (TTI) mismatch failure mode. When TTI mismatch condition occurs, this indicates
                          the consequent action taken, e.g. whether or not to raise an alarm.
                        type: str
                        required: false
                        choices:
                        - none
                        - alarm-only
                        - squelch-traffic
                      mismatch_mode:
                        description: The trail trace identifier (TTI) mismatch mode, indicating which fields of the TTI overhead are used for
                          trace mismatch detection.
                        type: str
                        required: false
                        choices:
                        - operator-only
                        - sapi
                        - dapi
                        - sapi-and-dapi
                      tx_dapi:
                        description: The destination access point identifier (DAPI) portion of the transmitted trace string, up to 15 characters,
                          excluding the first byte in the TTI DAPI overhead, which is implicitly always null.
                        type: str
                        required: false
                      tx_oper:
                        description: The operator-specific portion of the transmitted trace string, up to 32 characters. Ignored if tx-oper-mode
                          is 'automatic'.
                        type: str
                        required: false
                      tx_oper_mode:
                        description: Specifies whether to allow manual provisioning of the transmitted TTI string, or let the system assign this
                          value automatically based on a pre-defined format.
                        type: str
                        required: false
                        choices:
                        - manual
                        - automatic
                      tx_sapi:
                        description: The source access point identifier (SAPI) portion of the transmitted trace string, up to 15 characters, excluding
                          the first byte in the TTI SAPI overhead, which is implicitly always null.
                        type: str
                        required: false
      state:
        description: Port administrative and operational states.
        type: dict
        suboptions:
          admin_state:
            description: The configured administrative state of the port.
            type: str
            required: false
            choices:
            - enabled
            - disabled
    key: port-id
  state:
    description:
    - The state of the configuration
    type: str
    choices:
    - merged
    default: merged

"""
EXAMPLES = """
# Using merged

- name: Disable port
  ciena.waveserver5.waveserver5_ports:
    config:
      - port_id: 5-1
        state:
          admin_state: disabled
    state: merged
- name: Enable port
  ciena.waveserver5.waveserver5_ports:
    config:
      - port_id: 5-1
        state:
          admin_state: enabled
    state: merged
"""

RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
xml:
  description: The set of xml commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<system xmlns="http://openconfig.net/yang/system"><config><hostname>foo</hostname></config></system>']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.argspec.ports.ports import (
    PortsArgs,
)
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.config.ports.ports import (
    Ports,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=PortsArgs.argument_spec, supports_check_mode=True)

    result = Ports(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
