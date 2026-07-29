"""Utility functions for counting characteristics in strings."""


def _validate_text(value, parameter_name):
    """Validate that the provided value is a string."""
    if not isinstance(value, str):
        raise TypeError(f"{parameter_name} must be a string")


def count_vowels(text):
    """Count the number of vowels in the provided text."""
    _validate_text(text, "text")
    vowels = "aeiouAEIOU"
    return sum(1 for character in text if character in vowels)


def count_words(text):
    """Count words separated by whitespace in the provided text."""
    _validate_text(text, "text")
    return len(text.split())
