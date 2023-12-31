#!/usr/bin/env python3

# Copyright (c) Laserfiche.
# Licensed under the MIT License. See LICENSE in the project root for license information.

import sys

from utility.lf_arg_parser.src.lf_arg_parser import get_argument_map
from src.mirror import YourScriptMethod as Invoker

if __name__ == "__main__":
    # Inputs can be automatically parsed with the provided function
    # Or parsed manually via 'sys.argv'
    inputs = get_argument_map(sys.argv)
    outputs = Invoker(inputs)

    # Output can be printed to the console in `key:value` pairs format
    # remote agent will parse the output and return it to the caller
    for key, value in outputs.items():
        print(f"{key}:{value}")
