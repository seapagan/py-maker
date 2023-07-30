"""Subclass the Prompt class from Rich to add a few features.

I have a PR open to add these features to Rich, but until it is merged (if it is
merged) I will use this subclass.

Currently only makes the choices case-insensitive.
"""
from rich.prompt import Confirm as RichConfirm
from rich.prompt import InvalidResponse
from rich.prompt import Prompt as RichPrompt
from rich.prompt import PromptType


class Confirm(RichConfirm):
    """Just so we can import it from the same place as our Prompt.

    Saves importing from the Rich library.
    """


class Prompt(RichPrompt):
    """Override the Prompt class to make choices case-insensitive."""

    def check_choice(self, value: str) -> bool:
        """Check value is in the list of valid choices.

        Args:
            value (str): Value entered by user.

        Returns:
            bool: True if choice was valid, otherwise False.
        """
        assert self.choices is not None  # nosec
        return value.strip().lower() in [
            choice.lower() for choice in self.choices
        ]

    def process_response(self, value: str) -> PromptType:  # type: ignore
        """Process response from user, convert to prompt type.

        Args:
            value (str): String typed by user.

        Raises:
            InvalidResponse: If ``value`` is invalid.

        Returns:
            PromptType: The value to be returned from ask method.
        """
        value = value.strip()
        try:
            return_value: PromptType = self.response_type(value)  # type: ignore
        except ValueError as exc:
            raise InvalidResponse(self.validate_error_message) from exc

        if self.choices is not None:
            if not self.check_choice(value):
                raise InvalidResponse(self.illegal_choice_message)

            # return the original choice, not the lower case version
            return_value = self.response_type(  # type: ignore
                self.choices[
                    [choice.lower() for choice in self.choices].index(
                        value.lower()
                    )
                ]
            )
        return return_value
