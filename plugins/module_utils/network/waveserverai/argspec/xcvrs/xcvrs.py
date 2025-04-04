#
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
The arg spec for the waveserverai_xcvrs module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class XcvrsArgs(object):  # pylint: disable=R0903
    """The arg spec for the waveserverai_xcvrs module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "type": "list",
            "elements": "dict",
            "options": {
                "xcvr_id": {"type": "str", "required": True},
                "properties": {
                    "type": "dict",
                    "options": {
                        "mode": {
                            "type": "str",
                            "choices": [
                                "blank",
                                "OCH",
                                "OTM",
                                "OSC",
                                "OSC-Add-Drop",
                                "10GE",
                                "4x10GE",
                                "40GE",
                                "100GE",
                                "400GE",
                                "400GE-ZR",
                                "400GE-ZR+",
                                "4x100GE",
                                "4x100GE-ZR",
                                "4x100GE-ZR+",
                                "OTL4.4",
                                "OTLC.4",
                                "FOIC1.4",
                                "FOIC4.8",
                                "35-100",
                                "35-150",
                                "35-200",
                                "35-250",
                                "56-100",
                                "56-150",
                                "56-200",
                                "56-250",
                                "56-300",
                                "56-350",
                                "56-400",
                                "70-300-O",
                                "70-400-O",
                                "70-400-E",
                                "65-300-E",
                                "65-400-E",
                                "63-200-O",
                                "63-400-O",
                                "60-400-E-ZR",
                                "60-400-E-ZR+",
                                "60-200-E",
                                "58-200-O",
                                "35-200-O",
                                "31.5-100-O",
                                "31.5-200-O",
                                "95-200-O",
                                "95-250-O",
                                "95-300-O",
                                "95-350-O",
                                "95-400-O",
                                "95-450-O",
                                "95-500-O",
                                "95-550-O",
                                "95-600-O",
                                "95-650-O",
                                "95-700-O",
                                "95-750-O",
                                "95-800-O",
                                "95-200-E",
                                "95-250-E",
                                "95-300-E",
                                "95-350-E",
                                "95-400-E",
                                "95-450-E",
                                "95-500-E",
                                "95-550-E",
                                "95-600-E",
                                "95-650-E",
                                "95-700-E",
                                "95-750-E",
                                "95-800-E",
                                "91.6-200-O",
                                "91.6-250-O",
                                "91.6-300-O",
                                "91.6-350-O",
                                "91.6-400-O",
                                "91.6-450-O",
                                "91.6-500-O",
                                "91.6-550-O",
                                "91.6-600-O",
                                "91.6-650-O",
                                "91.6-700-O",
                                "91.6-750-O",
                                "91.6-800-O",
                                "91.6-200-E",
                                "91.6-250-E",
                                "91.6-300-E",
                                "91.6-350-E",
                                "91.6-400-E",
                                "91.6-450-E",
                                "91.6-500-E",
                                "91.6-550-E",
                                "91.6-600-E",
                                "91.6-650-E",
                                "91.6-700-E",
                                "91.6-750-E",
                                "91.6-800-E",
                                "89.3-200-O",
                                "89.3-250-O",
                                "89.3-300-O",
                                "89.3-350-O",
                                "89.3-400-O",
                                "89.3-450-O",
                                "89.3-500-O",
                                "89.3-550-O",
                                "89.3-600-O",
                                "89.3-650-O",
                                "89.3-700-O",
                                "89.3-750-O",
                                "89.3-800-O",
                                "89.3-200-E",
                                "89.3-250-E",
                                "89.3-300-E",
                                "89.3-350-E",
                                "89.3-400-E",
                                "89.3-450-E",
                                "89.3-500-E",
                                "89.3-550-E",
                                "89.3-600-E",
                                "89.3-650-E",
                                "89.3-700-E",
                                "89.3-750-E",
                                "89.3-800-E",
                                "71.3-200-O",
                                "71.3-250-O",
                                "71.3-300-O",
                                "71.3-350-O",
                                "71.3-400-O",
                                "71.3-450-O",
                                "71.3-500-O",
                                "71.3-550-O",
                                "71.3-600-O",
                                "71.3-200-E",
                                "71.3-250-E",
                                "71.3-300-E",
                                "71.3-350-E",
                                "71.3-400-E",
                                "71.3-450-E",
                                "71.3-500-E",
                                "71.3-550-E",
                                "71.3-600-E",
                                "69.5-200-O",
                                "69.5-250-O",
                                "69.5-300-O",
                                "69.5-350-O",
                                "69.5-400-O",
                                "69.5-450-O",
                                "69.5-500-O",
                                "69.5-550-O",
                                "69.5-600-O",
                                "69.5-200-E",
                                "69.5-250-E",
                                "69.5-300-E",
                                "69.5-350-E",
                                "69.5-400-E",
                                "69.5-450-E",
                                "69.5-500-E",
                                "69.5-550-E",
                                "69.5-600-E",
                                "93.3-200-O",
                                "93.3-250-O",
                                "93.3-300-O",
                                "93.3-350-O",
                                "93.3-400-O",
                                "93.3-450-O",
                                "93.3-500-O",
                                "93.3-550-O",
                                "93.3-600-O",
                                "93.3-650-O",
                                "93.3-700-O",
                                "93.3-750-O",
                                "93.3-800-O",
                                "93.3-200-E",
                                "93.3-250-E",
                                "93.3-300-E",
                                "93.3-350-E",
                                "93.3-400-E",
                                "93.3-450-E",
                                "93.3-500-E",
                                "93.3-550-E",
                                "93.3-600-E",
                                "93.3-650-E",
                                "93.3-700-E",
                                "93.3-750-E",
                                "93.3-800-E",
                                "90-200-O",
                                "90-250-O",
                                "90-300-O",
                                "90-350-O",
                                "90-400-O",
                                "90-450-O",
                                "90-500-O",
                                "90-550-O",
                                "90-600-O",
                                "90-650-O",
                                "90-700-O",
                                "90-750-O",
                                "90-800-O",
                                "90-200-E",
                                "90-250-E",
                                "90-300-E",
                                "90-350-E",
                                "90-400-E",
                                "90-450-E",
                                "90-500-E",
                                "90-550-E",
                                "90-600-E",
                                "90-650-E",
                                "90-700-E",
                                "90-750-E",
                                "90-800-E",
                                "85-200-O",
                                "85-250-O",
                                "85-300-O",
                                "85-350-O",
                                "85-400-O",
                                "85-450-O",
                                "85-500-O",
                                "85-550-O",
                                "85-600-O",
                                "85-650-O",
                                "85-700-O",
                                "85-750-O",
                                "85-800-O",
                                "85-200-E",
                                "85-250-E",
                                "85-300-E",
                                "85-350-E",
                                "85-400-E",
                                "85-450-E",
                                "85-500-E",
                                "85-550-E",
                                "85-600-E",
                                "85-650-E",
                                "85-700-E",
                                "85-750-E",
                                "85-800-E",
                                "82-200-O",
                                "82-250-O",
                                "82-300-O",
                                "82-350-O",
                                "82-400-O",
                                "82-450-O",
                                "82-500-O",
                                "82-550-O",
                                "82-600-O",
                                "82-650-O",
                                "82-700-O",
                                "82-750-O",
                                "82-800-O",
                                "82-200-E",
                                "82-250-E",
                                "82-300-E",
                                "82-350-E",
                                "82-400-E",
                                "82-450-E",
                                "82-500-E",
                                "82-550-E",
                                "82-600-E",
                                "82-650-E",
                                "82-700-E",
                                "82-750-E",
                                "82-800-E",
                                "107-200-O",
                                "107-200-E",
                                "107-250-O",
                                "107-250-E",
                                "107-300-O",
                                "107-300-E",
                                "107-350-O",
                                "107-350-E",
                                "107-400-O",
                                "107-400-E",
                                "107-450-O",
                                "107-450-E",
                                "107-500-O",
                                "107-500-E",
                                "107-550-O",
                                "107-550-E",
                                "107-600-O",
                                "107-600-E",
                                "107-650-O",
                                "107-650-E",
                                "107-700-O",
                                "107-700-E",
                                "107-750-O",
                                "107-750-E",
                                "107-800-O",
                                "107-800-E",
                            ],
                            "required": True,
                        }
                    },
                },
                "state": {
                    "type": "dict",
                    "options": {"admin_state": {"type": "str", "choices": ["disabled", "enabled"]}},
                },
            },
        },
        "state": {"type": "str", "default": "merged", "choices": ["merged"]},
    }  # pylint: disable=C0301
