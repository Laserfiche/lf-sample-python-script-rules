import pytest
from ..lf_arg_parser import get_argument_map


@pytest.mark.parametrize("commands, expected", [
    (['node.exe', './some/path/script.js', 'k1=v1'], {'k1': 'v1'}),
    (['node.exe', './some/path/script.js', 'k1=v1', 'k2=v2'], {'k1': 'v1', 'k2': 'v2'}),
    (['node.exe', './some/path/script.js', 'k1=v1', 'k2='], {'k1': 'v1', 'k2': ''}),
    (['node.exe', './some/path/script.js', 'k1=a"bc'], {'k1': 'a"bc'}),
    (['node.exe', './some/path/script.js', 'k1=""'], {'k1': '""'}),
    (['node.exe', './some/path/script.js', '="abc"', 'k2=v2'], {'k2': 'v2'}),
    (['node.exe', './some/path/script.js'], {}),
])
def test_get_argument_map(commands, expected):
    """
    Test cases for the `getArgumentMap` function.
    """
    actual = get_argument_map(commands)
    assert actual == expected
