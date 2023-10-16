# Copyright (c) Laserfiche.
# Licensed under the MIT License. See LICENSE in the project root for license information.

import pytest
from ..src.translator import translate


@pytest.mark.parametrize("sentence, lang, expected_output", [
    ("Hello, how are you?", "es", "Hola, ¿cómo estás?"),
    ("I love programming", "fr", "J'adore la programmation"),
    ("This is a test", "de", "Dies ist ein Test")
])
def test_translate(sentence, lang, expected_output):
    assert translate(sentence, lang) == expected_output
