#!/usr/bin/python
#
# Copyright: (c) 2025 Ciena Corp
# Copyright 2019 Red Hat
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: waveserverai_command
author:
  - Ciena
short_description: Run commands on remote devices running Ciena Waveserver Ai
description:
- Sends arbitrary commands to a Waveserver Ai node and returns the results read from the device.
  This module includes an argument that will cause the module to wait for a specific condition
  before returning or timing out if the condition is not met.
options:
  commands:
    description:
    - List of commands to send to the remote Waveserver Ai device over the configured provider.
      The resulting output from the command is returned. If the I(wait_for) argument is provided,
      the module is not returned until the condition is satisfied or the number of retries has
      expired. If a command sent to the device requires answering a prompt, it is possible to pass
      a dict containing I(command), I(answer) and I(prompt). Common answers are 'y' or "\\r"
      (carriage return, must be double quotes). See examples.
    required: true
    type: list
    elements: raw
  wait_for:
    description:
    - List of conditions to evaluate against the output of the command. The task will wait for
      each condition to be true before moving forward. If the conditional is not true within the
      configured number of retries, the task fails. See examples.
    aliases:
    - waitfor
    type: list
    elements: str
  match:
    description:
    - The I(match) argument is used in conjunction with the I(wait_for) argument to specify the
      match policy. Valid values are C(all) or C(any). If the value is set to C(all) then all
      conditionals in the wait_for must be satisfied. If the value is set to C(any) then only one
      of the values must be satisfied.
    default: all
    type: str
    choices:
    - any
    - all
  retries:
    description:
    - Specifies the number of retries a command should be tried before it is considered failed.
      The command is run on the target device every retry and evaluated against the I(wait_for)
      conditions.
    default: 10
    type: int
  interval:
    description:
    - Configures the interval in seconds to wait between retries of the command. If the command
      does not pass the specified conditions, the interval indicates how long to wait before trying
      the command again.
    default: 1
    type: int
notes:
- Requires an SSH-based connection type, such as C(connection=network_cli).
"""

EXAMPLES = """
- name: run software show on remote devices
  ciena.waveserverai.waveserverai_command:
    commands: software show

- name: run software show and check to see if output contains Normal
  ciena.waveserverai.waveserverai_command:
    commands: software show
    wait_for: result[0] contains Normal

- name: run multiple commands on remote nodes
  ciena.waveserverai.waveserverai_command:
    commands:
      - software show
      - xcvr show

- name: run multiple commands and evaluate the output
  ciena.waveserverai.waveserverai_command:
    commands:
      - software show
      - xcvr show
    wait_for:
      - result[0] contains Installed
      - result[1] contains Port

"""

RETURN = """
stdout:
  description: The set of responses from the commands
  returned: always apart from low level errors (such as action plugin)
  type: list
  sample: ['...', '...']
stdout_lines:
  description: The value of stdout split into a list
  returned: always apart from low level errors (such as action plugin)
  type: list
  sample: [['...', '...'], ['...'], ['...']]
failed_conditions:
  description: The list of conditionals that have failed
  returned: failed
  type: list
  sample: ['...', '...']
"""

import time

from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.parsing import Conditional
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    transform_commands,
    to_lines,
)
from ansible_collections.ciena.waveserverai.plugins.module_utils.network.waveserverai.waveserverai import (
    run_commands,
)


def parse_commands(module, warnings):
    return transform_commands(module)


def main():
    argument_spec = dict(
        commands=dict(type="list", required=True, elements="raw"),
        wait_for=dict(type="list", aliases=["waitfor"], elements="str"),
        match=dict(default="all", choices=["all", "any"], type="str"),
        retries=dict(default=10, type="int"),
        interval=dict(default=1, type="int"),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    warnings = []
    result = {"changed": False, "warnings": warnings}

    commands = parse_commands(module, warnings)

    wait_for = module.params["wait_for"] or []
    try:
        conditionals = [Conditional(condition) for condition in wait_for]
    except AttributeError as exc:
        module.fail_json(msg=to_text(exc))

    retries = module.params["retries"]
    interval = module.params["interval"]
    match = module.params["match"]

    while retries > 0:
        responses = run_commands(module, commands)
        for conditional in list(conditionals):
            if conditional(responses):
                if match == "any":
                    conditionals = []
                    break
                conditionals.remove(conditional)
        if not conditionals:
            break
        time.sleep(interval)
        retries -= 1

    if conditionals:
        failed_conditions = [conditional.raw for conditional in conditionals]
        msg = "One or more conditional statements have not been satisfied"
        module.fail_json(msg=msg, failed_conditions=failed_conditions)

    result.update({"stdout": responses, "stdout_lines": list(to_lines(responses))})
    module.exit_json(**result)


if __name__ == "__main__":
    main()
