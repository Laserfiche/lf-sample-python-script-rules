#!/usr/bin/env python3

import sys

from utility.lf_arg_parser.src.lf_arg_parser import get_argument_map
from src.translator import translate

if __name__ == "__main__":
    # Inputs can be automatically parsed with the provided function
    # Or parsed manually via 'sys.argv'
    inputsMap = get_argument_map(sys.argv)

    sentence = inputsMap['Sentence']
    language = inputsMap["LanguageCode"]
    translated = translate(sentence, language)

    # Output can be printed to the console in `key:value` pairs format
    # remote agent will parse the output and return it to the caller
    print(f"translated : {translated}")
