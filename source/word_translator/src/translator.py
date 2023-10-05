from translate import Translator


def translate(sentence: str, lang: str) -> str:
    """
    Translates a sentence into the specified language.

    :param sentence: The sentence to translate.
    :type sentence: str
    :param lang: The language to translate the sentence into.
    :type lang: str
    :return: The translated sentence.
    :rtype: str
    """

    translator = Translator(to_lang=lang)
    return translator.translate(sentence)
