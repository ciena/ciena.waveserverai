#
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
The arg spec for the waveserverai_xcvr module
"""


class XcvrArgs(object):  # pylint: disable=R0903
    """The arg spec for the waveserverai_xcvr module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "properties": {
                    "options": {
                        "mode": {
                            "choices": [
                                "100GE",
                                "OTL4.4",
                                "56-100",
                                "56-150",
                                "56-200",
                                "56-250",
                                "56-300",
                                "56-350",
                                "56-400",
                                "35-100",
                                "35-150",
                                "35-250",
                                "OCH",
                                "OTM",
                                "4x10GE",
                                "35-200",
                                "OSC",
                                "OTLC.4",
                                "OSC-ADD-DROP",
                            ],
                            "type": "str",
                        }
                    },
                    "type": "dict",
                },
                "xcvr-id": {"required": True, "type": "str"},
            },
            "type": "list",
        },
        "state": {
            "choices": ["merged", "overridden"],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
