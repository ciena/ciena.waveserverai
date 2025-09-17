# (c) 2025 Ciena Corp.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
name: waveserverai
author:
  - Ciena
short_description: Use waveserverai cliconf to run commands on Ciena Waveserver Ai platform
description:
  - This waveserverai plugin provides low level abstraction APIs for sending and receiving
    CLI commands from Ciena Waveserver Ai network devices.
"""

import json
import re

from ansible.errors import AnsibleConnectionFailure, AnsibleError
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Mapping
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
from ansible.plugins.cliconf import CliconfBase


class Cliconf(CliconfBase):
    def get_device_info(self):
        return {"network_os": "ciena.waveserverai.waveserverai"}

    def get_config(self, source="running", flags=None, format="text"):
        command = "configuration show"
        try:
            return self.send_command(command)
        except AnsibleConnectionFailure:
            # Some platforms may not support a running-config view over CLI.
            # Re-raise so callers get a clear failure rather than silent None.
            raise

    def edit_config(self, candidate=None, commit=False, comment=None):
        raise AnsibleError("Configuration editing is not supported over CLI for Waveserver Ai")

    def get(
        self,
        command=None,
        prompt=None,
        answer=None,
        sendonly=False,
        newline=True,
        output=None,
        check_all=False,
    ):
        if not command:
            raise ValueError("must provide value of command to execute")
        if output:
            raise ValueError("'output' value %s is not supported for get" % output)

        return self.send_command(
            command=command,
            prompt=prompt,
            answer=answer,
            sendonly=sendonly,
            newline=newline,
            check_all=check_all,
        )

    def run_commands(self, commands=None, check_rc=True):
        if commands is None:
            raise ValueError("'commands' value is required")

        responses = []
        for cmd in to_list(commands):
            if not isinstance(cmd, Mapping):
                cmd = {"command": cmd}

            output = cmd.pop("output", None)
            if output:
                raise ValueError("'output' value %s is not supported for run_commands" % output)

            try:
                out = self.send_command(**cmd)
            except AnsibleConnectionFailure as exc:
                if check_rc:
                    raise
                out = getattr(exc, "err", exc)

            responses.append(out)

        return responses

    def get_capabilities(self):
        result = super(Cliconf, self).get_capabilities()
        return json.dumps(result)
