from katas.first_non_repeating_character.first_non_repeating_character import (
    first_non_repeating_character,
)


def test_handles_empty_input():
    # Arrange
    test_input = ""
    expected = ""
    # Act
    result = first_non_repeating_character(test_input)
    # Assert
    assert result == expected
