#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Red Hat Inc.
# Copyright (c) 2024, Guido Grazioli <ggraziol@redhat.com>
# Apache License, Version 2.0 (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: tail_grep
short_description: Tail a logfile until a regex matcher is found or a timeout triggers
description:
     - This module is used to follow some application logfile and return successfully when
       a search string or regex is found; otherwise fail after a timeout.
options:
  path:
    description:
      - The file on the remote system to tail.
    type: path
    required: true
  regex:
    description:
      - The string or regular expression to search in the file.
    type: str
    required: true
  timeout:
    description:
      - After how many seconds to exit unsuccessfully without having found the search regex.
    required: false
    type: int
    default: 60
  from_regex:
    description:
      - Backwards from end of file, lines preceeding this string will not be considered for
        matching regex. By default, the whole file is read. If `$` is used, start from the
        first line written after the file is opened.
    required: false
    type: str
    default: ''
  delay:
    description:
      - How many seconds to wait after opening the file before starting to look for the regex.
    required: false
    type: int
    default: 0
extends_documentation_fragment:
    - action_common_attributes
attributes:
  check_mode:
    support: none
  diff_mode:
    support: none
  platform:
    platforms: posix
author:
    - Guido Grazioli (@guidograzioli)
'''

EXAMPLES = r'''
- name: Tail activemq log until the successful start status code is found
  ansible.builtin.tail_grep:
    path: /var/log/activemq/artemis.log
    regex: AMQ220010
'''

RETURN = r'''
content:
    description: The full string that was matched by the search regex
    returned: success
    type: str
    sample: "Application has been started successfully."
source:
    description: Actual path of file opened
    returned: success
    type: str
    sample: "/var/log/messages"
'''

import errno
import re
import time

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native


def amq_argument_spec():
    """
    Returns argument_spec of options

    :return: argument_spec dict
    """
    return dict(
        path=dict(type='path', required=True),
        regex=dict(type='str', required=True),
        timeout=dict(type='int', required=False, default=60),
        from_regex=dict(type='str', required=False, default=''),
        delay=dict(type='int', required=False, default=0)
    )


# from https://stackoverflow.com/a/54263201/389099
def follow(file, sleep_sec=0.1, timeout_sec=60):
    """ Yield each line from a file as they are written.
    `sleep_sec` is the time to sleep after empty reads. """
    line = ''
    ts = time.time()
    while True:
        tmp = file.readline()
        if tmp is not None and tmp != "":
            line += tmp
            if line.endswith("\n"):
                yield line
                line = ''
        elif sleep_sec:
            time.sleep(sleep_sec)
            if (time.time() >= (ts + timeout_sec)):
                raise Exception("timeout reached without finding search string in file")


def main():
    module = AnsibleModule(argument_spec=amq_argument_spec(), supports_check_mode=False)

    source = module.params['path']
    regex = module.params['regex']
    timeout = module.params['timeout']
    delay = module.params['delay']

    try:
        with open(source, 'r') as source_fh:
            time.sleep(delay)
            for line in follow(source_fh, 0.25, timeout):
                if re.match(regex, line):
                    break
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source
        elif e.errno == errno.EISDIR:
            msg = "source is a directory and must be a file: %s" % source
        else:
            msg = "unable to read file: %s" % to_native(e, errors='surrogate_then_replace')

        module.fail_json(msg)

    except (Exception) as e:
        module.fail_json(e.args)

    module.exit_json(content=line, source=source)


if __name__ == '__main__':
    main()
