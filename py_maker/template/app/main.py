"""Example entry point for the main application loop."""


class App:
    """Main application class."""

    def __init__(self) -> None:
        """Initialize the application."""
        pass

    def __call__(self) -> None:
        """Call the application."""
        print("Welcome!")


app = App()


if __name__ == "__main__":
    app()
