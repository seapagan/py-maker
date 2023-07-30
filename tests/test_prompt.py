"""Test our changes to the Rich Prompt class."""
import pytest

from py_maker.prompt import InvalidResponse, Prompt


def test_prompt_check_choice():
    """Test that check_choice is case-insensitive."""
    prompt = Prompt(
        "What is your favorite color?", choices=["Red", "Green", "Blue"]
    )
    assert prompt.check_choice("red")
    assert prompt.check_choice("GREEN")
    assert not prompt.check_choice("yellow")


def test_prompt_process_response():
    """Test that process_response returns the original choice.

    Even if the users types it in a different case, it should always return
    the original choice.
    """
    prompt = Prompt(
        "What is your favorite color?", choices=["Red", "Green", "Blue"]
    )
    assert prompt.process_response("red") == "Red"
    assert prompt.process_response("GREEN") == "Green"
    with pytest.raises(InvalidResponse):
        prompt.process_response("yellow")
