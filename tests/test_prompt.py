"""Test suite for custom prompt classes in py_maker.prompt."""

import io

import pytest
from rich.console import Console

from py_maker.prompt import Confirm, InvalidResponse, Prompt


def test_confirm_yes() -> None:
    """Test Confirm.ask for a 'yes' response."""
    user_input = "y\n"
    console = Console(file=io.StringIO())
    answer = Confirm.ask(
        "Continue?", console=console, stream=io.StringIO(user_input)
    )
    assert answer is True


def test_confirm_no() -> None:
    """Test Confirm.ask for a 'no' response."""
    user_input = "n\n"
    console = Console(file=io.StringIO())
    answer = Confirm.ask(
        "Continue?", console=console, stream=io.StringIO(user_input)
    )
    assert answer is False


def test_prompt_check_choice() -> None:
    """Test that check_choice is case-insensitive."""
    prompt = Prompt(
        "What is your favorite color?", choices=["Red", "Green", "Blue"]
    )
    assert prompt.check_choice("red")
    assert prompt.check_choice("GREEN")
    assert not prompt.check_choice("yellow")


def test_prompt_process_response() -> None:
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


def test_prompt_process_response_value_error() -> None:
    """Test process_response raises ValueError for invalid data."""
