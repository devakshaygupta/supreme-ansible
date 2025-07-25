#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
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
The module file for vyos_lldp_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: vyos_lldp_interfaces
version_added: '1.0.0'
short_description: LLDP interfaces resource module
description: This module manages attributes of lldp interfaces on VyOS network devices.
notes:
- Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025
- This module works with connection C(ansible.netcommon.network_cli).
  See L(the VyOS OS Platform Options,../network/user_guide/platform_vyos.html).
author:
 - Rohit Thakur (@rohitthakur2590)
options:
  config:
    description: A list of LLDP interfaces configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the LLDP interface.
        type: str
        required: true
      enable:
        default: true
        description:
        - Disable LLDP on the interfaces.
        type: bool
      location:
        description:
        - LLDP-MED location data.
        type: dict
        suboptions:
          coordinate_based:
            description:
            - Coordinate-based location.
            type: dict
            suboptions:
              altitude:
                description: Altitude in meters.
                type: int
              datum:
                description: Coordinate datum type.
                type: str
                choices:
                - WGS84
                - NAD83
                - MLLW
              latitude:
                description: Latitude.
                type: str
                required: true
              longitude:
                description: Longitude.
                type: str
                required: true
          elin:
            description: Emergency Call Service ELIN number (between 10-25 numbers).
            type: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VyOS device
        by executing the command B(show configuration commands | grep lldp).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - rendered
    - parsed
    - gathered
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep lldp
#
- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
      - name: eth1
        location:
          elin: 0000000911
      - name: eth2
        location:
          coordinate_based:
            altitude: 2200
            datum: WGS84
            longitude: 222.267255W
            latitude: 33.524449N
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": {}
#
#    "commands": [
#        "set service lldp interface eth1 location elin '0000000911'",
#        "set service lldp interface eth1",
#        "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth2 location coordinate-based altitude '2200'",
#        "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#        "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth2 location coordinate-based altitude '2200'",
#        "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#        "set service lldp interface eth2"
#    ]
#
# "after": {
#      "location": {
#          "coordinate_based": {
#              "altitude": 2200,
#              "datum": "WGS84",
#              "latitude": "33.524449N",
#              "longitude": "222.267255W"
#          }
#      },
#      "name": "eth2"
#  },
#  {
#      "location": {
#          "elin": "0000000911"
#          }
#      },
#      "name": "eth1"
#  }
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 location elin '0000000911'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'


# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 location elin '0000000911'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'
#
- name: >-
    Replace device configurations of listed LLDP interfaces with provided
    configurations
  vyos.vyos.vyos_lldp_interfaces:
    config:
      - name: eth2
        location:
          elin: 0000000911
      - name: eth1
        location:
          coordinate_based:
            altitude: 2200
            datum: WGS84
            longitude: 222.267255W
            latitude: 33.524449N
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "elin": "0000000911"
#            },
#            "name": "eth1"
#        }
#    ]
#
#    "commands": [
#        "delete service lldp interface eth2 location",
#        "set service lldp interface eth2 'disable'",
#        "set service lldp interface eth2 location elin '0000000911'",
#        "delete service lldp interface eth1 location",
#        "set service lldp interface eth1 'disable'",
#        "set service lldp interface eth1 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth1 location coordinate-based altitude '2200'",
#        "set service lldp interface eth1 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth1 location coordinate-based longitude '222.267255W'"
#    ]
#
#    "after": {
#        "location": {
#            "elin": "0000000911"
#        },
#        "name": "eth2"
#    },
#    {
#        "location": {
#            "coordinate_based": {
#                "altitude": 2200,
#                "datum": "WGS84",
#                "latitude": "33.524449N",
#                "longitude": "222.267255W"
#            }
#        },
#        "name": "eth1"
#    }
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 'disable'
# set service lldp interface eth1 location coordinate-based altitude '2200'
# set service lldp interface eth1 location coordinate-based datum 'WGS84'
# set service lldp interface eth1 location coordinate-based latitude '33.524449N'
# set service lldp interface eth1 location coordinate-based longitude '222.267255W'
# set service lldp interface eth2 'disable'
# set service lldp interface eth2 location elin '0000000911'


# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 'disable'
# set service lldp interface eth1 location coordinate-based altitude '2200'
# set service lldp interface eth1 location coordinate-based datum 'WGS84'
# set service lldp interface eth1 location coordinate-based latitude '33.524449N'
# set service lldp interface eth1 location coordinate-based longitude '222.267255W'
# set service lldp interface eth2 'disable'
# set service lldp interface eth2 location elin '0000000911'
#
- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
      - name: eth2
        location:
          elin: 0000000911

    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#    {
#      "enable": false,
#      "elin": "0000000911",
#      "name": "eth2"
#    },
#    {
#      "enable": false,
#      "location": {
#        "coordinate_based": {
#          "altitude": 2200,
#          "datum": "WGS84",
#          "latitude": "33.524449N",
#          "longitude": "222.267255W"
#        }
#      },
#      "name": "eth1"
#    }
#  ]
#
# "commands": [
#    "delete service lldp interface eth2 location",
#    "delete service lldp interface eth2 disable",
#    "set service lldp interface eth2 location elin 0000000911"
#  ]
#
# "after": [
#    {
#      "location": {
#        "elin": 0000000911
#      },
#      "name": "eth2"
#    }
#  ]
#
#
# After state
# ------------
#
# vyos@vyos# run show configuration commands | grep lldp
# set service lldp interface eth2 location elin '0000000911'


# Using deleted
#
# Before state
# -------------
#
# vyos@vyos# run show configuration commands | grep lldp
# set service lldp interface eth2 location elin '0000000911'
#
- name: Delete LLDP interface attributes of given interfaces.
  vyos.vyos.vyos_lldp_interfaces:
    config:
      - name: eth2
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#  "before": [
#       {
#          "location": {
#              "elin": 0000000911
#          },
#          "name": "eth2"
#      }
#  ]
#  "commands": [
#      "delete service lldp interface eth2"
#  ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep lldp
# set service 'lldp'


# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep lldp
# set service lldp interface eth1 location elin '0000000911'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'
#
- name: Gather listed lldp interfaces from running configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "location": {
#                 "coordinate_based": {
#                     "altitude": 2200,
#                     "datum": "WGS84",
#                     "latitude": "33.524449N",
#                     "longitude": "222.267255W"
#                 }
#             },
#             "name": "eth2"
#         },
#         {
#             "location": {
#                 "elin": "0000000911"
#             },
#             "name": "eth1"
#         }
#     ]
#
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep lldp
# set service lldp interface eth1 location elin '0000000911'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'


# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_lldp_interfaces:
    config:
      - name: eth1
        location:
          elin: 0000000911
      - name: eth2
        location:
          coordinate_based:
            altitude: 2200
            datum: WGS84
            longitude: 222.267255W
            latitude: 33.524449N
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#         "set service lldp interface eth1 location elin '0000000911'",
#         "set service lldp interface eth1",
#         "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#         "set service lldp interface eth2 location coordinate-based altitude '2200'",
#         "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#         "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#         "set service lldp interface eth2"
#     ]


# Using parsed
#
#
- name: Parsed the commands to provide structured configuration.
  vyos.vyos.vyos_lldp_interfaces:
    running_config:
      "set service lldp interface eth1 location elin '0000000911'
       set service lldp interface eth2 location coordinate-based altitude '2200'
       set service lldp interface eth2 location coordinate-based datum 'WGS84'
       set service lldp interface eth2 location coordinate-based latitude '33.524449N'
       set service lldp interface eth2 location coordinate-based longitude '222.267255W'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "location": {
#                 "coordinate_based": {
#                     "altitude": 2200,
#                     "datum": "WGS84",
#                     "latitude": "33.524449N",
#                     "longitude": "222.267255W"
#                 }
#             },
#             "name": "eth2"
#         },
#         {
#             "location": {
#                 "elin": "0000000911"
#             },
#             "name": "eth1"
#         }
#     ]
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
    of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
    of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - "set service lldp interface eth2 'disable'"
    - "delete service lldp interface eth1 location"

"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.lldp_interfaces.lldp_interfaces import (
    Lldp_interfacesArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.lldp_interfaces.lldp_interfaces import (
    Lldp_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Lldp_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
