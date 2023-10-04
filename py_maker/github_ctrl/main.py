"""Define the GitHub class.

This is a class to encapsulate the GitHub API and is responsible for
authenticating with GitHub and performing the necessary operations.
"""
from github import Auth, Github
from github.GithubException import GithubException


def git_error(exc: Exception):
    """Display any errors cleanly during a git operation."""
    message = exc.data.get("message")
    error = exc.data.get("errors", None)
    error_message = ""
    if error:
        error_message = f"({error[0].get('message')})".capitalize()
    print(f"Error creating repository: {message} {error_message}")


class GitHub:
    """Define the main GitHub class."""

    def __init__(self, github_token: str = None, repo_name: str = None):
        """Initialize the GitHub class."""
        self.github_token = github_token
        if self.github_token is None:
            raise ValueError("GitHub token must be provided.")  # noqa: TRY003

        self._auth = Auth.Token(self.github_token)
        self._github = Github(auth=self._auth)
        self._user = self._github.get_user()

        # default to no repo name, this will need to be set before any
        # operations are performed.
        self.repo_name = repo_name

    def __del__(self):
        """Close the underlying Github object when we are done."""
        self._github.close()

    @property
    def user(self):
        """Return the GitHub user object."""
        return self._user

    @property
    def repo(self):
        """Return the GitHub repository object."""
        try:
            return self._user.get_repo(self.repo_name)
        except AssertionError:
            print(f"Repository '{self.repo_name}' does not exist.")

    def create_repo(self, repo_name: str = None, private: bool = False):
        """Create a new repository.

        Args:
            repo_name: The name of the repository to create.
            private: Whether the repository should be private or not.
        """
        if repo_name is None:
            raise ValueError(  # noqa: TRY003
                "Repository name must be provided."
            )

        self.repo_name = repo_name

        try:
            self._user.create_repo(repo_name, private=private)
        except GithubException as exc:
            git_error(exc)
