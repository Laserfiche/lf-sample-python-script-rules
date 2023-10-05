#!/usr/bin/env python3

import sys

from utility.lf_arg_parser.src.lf_arg_parser import get_argument_map
from src.mirror import YourScriptMethod as invoker


def main():
    # Inputs can be automatically parsed with the provided function
    # Or parsed manually via 'process.argv'
    inputs = get_argument_map(sys.argv)
    outputs = invoker(inputs)

    # Output can be printed to the console in key:value pairs format
    # remote agent will parse the output and return it to the caller
    for key, value in outputs.items():
        print(f"{key}:{value}")


if __name__ == "__main__":
    main()