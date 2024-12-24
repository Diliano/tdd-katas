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


def test_handles_single_character_input():
    # Arrange
    test_input = "c"
    expected = "c"
    # Act
    result = first_non_repeating_character(test_input)
    # Assert
    assert result == expected


def test_finds_non_repeating_character():
    # Arrange
    test_input = "racecar"
    expected = "e"
    # Act
    result = first_non_repeating_character(test_input)
    # Assert
    assert result == expected
