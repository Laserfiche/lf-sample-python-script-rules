import pytest
from ..src.mirror import YourScriptMethod


@pytest.mark.parametrize("input_value", ["aaa", "bbb", "ccc"])
def test_your_script_method(input_value):
    inputs = {"key": input_value}
    expected_output = {"key": input_value}

    actual_output = YourScriptMethod(inputs)

    assert actual_output == expected_output