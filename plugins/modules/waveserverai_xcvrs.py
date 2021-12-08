#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Ciena
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
The module file for waveserverai_xcvrs
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: waveserverai_xcvrs
version_added: 2.9
short_description: Manage XCVR on Ciena Waveserver Ai devices
description: This module provides declarative management of a transceiver
author: Ciena
options:
  config:
    description: A dictionary of XVCR options
    type: list
    elements: dict
    suboptions:
      xcvr-id:
        description:
        - Full name of xcvr, e.g. 1-1.
        type: str
        required: True
      properties:
        description:
        - A dictionary of properties to be configured on the xcvr.
        type: dict
        suboptions:
          mode:
            description:
              - Mode C(unit) should be of type string.
            choices:
              - 100GE
              - OTL4.4
              - 56-100
              - 56-150
              - 56-200
              - 56-250
              - 56-300
              - 56-350
              - 56-400
              - 35-100
              - 35-150
              - 35-250
              - OCH
              - OTM
              - 4x10GE
              - 35-200
              - OSC
              - OTLC.4
              - OSC-ADD-DROP
            type: str
  state:
    choices:
    - merged
    - overridden
    default: merged
    description:
    - The state the configuration should be left in
    type: str
"""
EXAMPLES = """
# Using merged

- name: Configure interfaces
  ciena.waveserverai.waveserverai_xcvrs:
    config:
      - name: 1-1
        properties:
          mode: 56-400
    operation: merged


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.argspec.xcvrs.xcvrs import (
    XcvrsArgs,
)
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.config.xcvrs.xcvrs import (
    Xcvrs,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=XcvrsArgs.argument_spec, supports_check_mode=True
    )

    result = Xcvrs(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
