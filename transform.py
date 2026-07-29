"""Utility functions for basic string transformations."""


def _validate_text(value, parameter_name):
    """Validate that the provided value is a string."""
    if not isinstance(value, str):
        raise TypeError(f"{parameter_name} must be a string")


def to_uppercase(text):
    """Convert text to uppercase."""
    _validate_text(text, "text")
    return text.upper()


def to_lowercase(text):
    """Convert text to lowercase."""
    _validate_text(text, "text")
    return text.lower()


def merge_strings(str1, str2, separator=""):
    """Merge two strings with an optional separator."""
    _validate_text(str1, "str1")
    _validate_text(str2, "str2")
    _validate_text(separator, "separator")
    return f"{str1}{separator}{str2}"