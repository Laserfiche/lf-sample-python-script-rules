# Copyright (c) Laserfiche.
# Licensed under the MIT License. See LICENSE in the project root for license information.

from translate import Translator


def translate(sentence: str, lang: str) -> str:
    """
    Translates a sentence into the specified language.
    Uses 'translate module'.  See https://pypi.org/project/translate/ for more information.

    :param sentence: The sentence to translate.
    :type sentence: str
    :param lang: The language to translate the sentence into.
                 See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes for valid language codes.
    :type lang: str
    :return: The translated sentence.
    :rtype: str
    """

    translator = Translator(to_lang=lang)
    return translator.translate(sentence)
