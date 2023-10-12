import pytest
from ..src.lf_arg_parser import get_argument_map


@pytest.mark.parametrize("commands, expected", [
    (['python', './some/path/script.py', 'k1=v1'], {'k1': 'v1'}),
    (['python', './some/path/script.py', 'k1=v1', 'k2=v2'], {'k1': 'v1', 'k2': 'v2'}),
    (['python', './some/path/script.py', 'k1=v1', 'k2='], {'k1': 'v1', 'k2': ''}),
    (['python', './some/path/script.py', 'k1=a"bc'], {'k1': 'a"bc'}),
    (['python', './some/path/script.py', 'k1=""'], {'k1': '""'}),
    (['python', './some/path/script.py', '="abc"', 'k2=v2'], {'k2': 'v2'}),
    (['python', './some/path/script.py'], {}),
])
def test_get_argument_map(commands, expected):
    """
    Test cases for the `getArgumentMap` function.
    """
    actual = get_argument_map(commands)
    assert actual == expected
