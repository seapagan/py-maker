"""Tests for the constants module."""
from py_maker import constants

LICENSE_DICT_SIZE = 2


def test_licenses() -> None:
    """Test that the licenses constant is a list of dictionaries."""
    assert isinstance(constants.LICENCES, list)
    assert all(
        isinstance(license_details, dict)
        for license_details in constants.LICENCES
    )
    assert all(
        len(license_details) == LICENSE_DICT_SIZE
        for license_details in constants.LICENCES
    )


def test_license_names() -> None:
    """Test that the license_names constant is a list of strings."""
    assert isinstance(constants.license_names, list)
    assert all(isinstance(name, str) for name in constants.license_names)


def test_exit_errors() -> None:
    """Test that the ExitErrors enum is an IntEnum."""
    assert issubclass(constants.ExitErrors, int)
    assert all(isinstance(error, int) for error in constants.ExitErrors)
