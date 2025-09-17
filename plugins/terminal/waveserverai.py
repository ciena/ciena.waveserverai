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

import re

from ansible.plugins.terminal import TerminalBase


class TerminalModule(TerminalBase):
    # mirror SAOS10 prompt handling with relaxed trailing whitespace
    terminal_stdout_re = [
        re.compile(rb"[\w+\-.:@/\[\]]+(?:\([^\)]+\)){0,3}[*]?>\s"),
        re.compile(rb"[\w+\-.:@/\[\]]+(?:\([^\)]+\)){0,3}[*]?#\s"),
        re.compile(rb"diag@\S+\$\s"),
    ]

    terminal_stderr_re = [
        re.compile(rb"SHELL PARSER FAILURE"),
        re.compile(rb"ERROR\:"),
        re.compile(rb"Error\:"),
    ]

    terminal_initial_prompt_newline = False
