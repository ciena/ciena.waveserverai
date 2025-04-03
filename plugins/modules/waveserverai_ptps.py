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
The module file for waveserverai_ptps
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
---
module: waveserverai_ptps
short_description: Waveserver Physical Termination Point (PTP) configuration and operational data.Manage the ptps ptps configuration of a Ciena
  waveserverai device
description: "Waveserver Physical Termination Point (PTP) configuration and operational data.\n List of PTP objects."
author: Ciena
options:
  config:
    description: List of PTP objects.
    type: list
    elements: dict
    suboptions:
      id:
        description: Identification information of this PTP instance.
        type: dict
        suboptions:
          label:
            description: Label of the PTP instance
            type: str
            required: false
      properties:
        description: All the configurable and operational data of this PTP instance.
        type: dict
        suboptions:
          type:
            description: Physical Termination Point type.
            type: str
            required: false
            choices:
            - unknown
            - WLAi
            - WLAi-iOPS
            - 4x25G
            - 10G
            - OCH
            - OSC
            - OSC-Add-Drop
            - OTM
            - WL5e
            - WL5n
            - 100G
            - 4x100G
            - 8x50G
            - 2x50G
            - 400ZR
          forward_error_correction:
            description: FEC - disabled, enabled, automatic. FEC format is determined by modem
            type: str
            required: false
            choices:
            - disabled
            - enabled
            - automatic
          is_coherent:
            description: Indicate whether or not this ptp can support coherent attributes
            type: bool
            required: false
          thresholds:
            description: Common container for PTP threshold configuration data.
            type: dict
            suboptions:
              fec_detected_degrade_threshold:
                description: FEC Signal Degrade configurable threshold, expressed in exponential notation, e.g. '1E-06' to '1E-09'.
                type: str
                required: false
              fec_excessive_degrade_threshold:
                description: FEC Signal Fail configurable threshold, expressed in exponential notation, e.g. '1E-06' to '1E-09'.
                type: str
                required: false
              hccs_db:
                description: High Correction Count Second (HCCS) Threshold, expressed in dB notation.
                type: float
                required: false
              pre_fec_sd_db:
                description: Pre-FEC Signal Degrade threshold value, expressed in dB notation.
                type: float
                required: false
              pre_fec_sf_db:
                description: Pre-FEC Signal Fail threshold value, expressed in dB notation.
                type: float
                required: false
          topology_adjacency:
            description: Container for PTP topology adjacency data.
            type: dict
            suboptions:
              port_in:
                description: Port in.
                type: str
                required: false
              port_out:
                description: Port out.
                type: str
                required: false
          transmitter:
            description: PTP transmitter related config and operational data fields.
            type: dict
            suboptions:
              state:
                description: Transmitter state (enabled or disabled) of the PTP. PTP Admin State cannot be changed to enabled unless the transmitter
                  state is enabled.
                type: str
                required: false
                choices:
                - disabled
                - enabled
                - not-applicable
          xcvr_type:
            description: Transceiver type of the XCVR that's associated with this PTP. Type depends on what is physically plugged in. Read only
              attribute.
            type: str
            required: false
            choices:
            - not-available
            - unsupported
            - QSFPplus
            - QSFP28
            - WaveLogic 3 Extreme
            - WaveLogic Ai
            - SFP
            - none
            - QSFP-DD
            - WaveLogic 5e
            - CFP2-DCO
      ptp_id:
        description: 'Unique, access identifier string of the PTP (e.g., ''1-1''). Key value for the PTP list. Read-only attribute. (Key for list:
          ptps)'
        type: str
        required: true
      state:
        description: State information of this PTP instance.
        type: dict
        suboptions:
          admin_state:
            description: Administrative state (enabled or disabled) of the PTP. If Admin State is set to enabled, majority of the PTP fields will
              no longer be modifiable. When PTP Transmitter State is Disabled, PTP Admin State cannot be changed from Disabled to Enabled.
            type: str
            required: false
            choices:
            - disabled
            - enabled
          spli_management:
            description: Whether or not Service Photonic Layer Interoperations management protocol is enabled on this PTP.
            type: str
            required: false
            choices:
            - disabled
            - enabled
    key: ptp-id
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

- name: Disable ptp
  ciena.waveserver5.waveserver5_ptps:
    config:
      - ptp_id: 5-1
        state:
          admin_state: disabled
    state: merged
- name: Enable ptp
  ciena.waveserver5.waveserver5_ptps:
    config:
      - ptp_id: 5-1
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
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.argspec.ptps.ptps import (
    PtpsArgs,
)
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.config.ptps.ptps import (
    Ptps,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=PtpsArgs.argument_spec, supports_check_mode=True)

    result = Ptps(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
