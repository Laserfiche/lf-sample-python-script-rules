# Copyright (c) Laserfiche.
# Licensed under the MIT License. See LICENSE in the project root for license information.

import sys
from typing import List, Dict


def get_argument_map(argument_list: List[str]) -> Dict[str, str]:
    """
    Parses the argument list and returns a dictionary of key-value pairs.

    :param argument_list: A list of command-line arguments.
    :type argument_list: list[str]
    :return: A dictionary of key-value pairs representing the parsed arguments.
    :rtype: dict[str, str]
    :raises Exception: If the argument list is invalid.
    """
    argument_map = {}
    if argument_list is None:
        raise Exception("Invalid arguments.")
    for arg in argument_list[1:len(argument_list):1]:
        try:
            if arg is not None:
                kv = arg.split('=', 1)
                if len(kv) == 2:  # '=' exists
                    key = kv[0]
                    if key is not None and len(key) > 0:
                        value = kv[1]
                        argument_map[key] = value
        except Exception as e:
            sys.stderr.write(f"Could not parse arguments: {str(e)}")
            raise e
    return argument_map
