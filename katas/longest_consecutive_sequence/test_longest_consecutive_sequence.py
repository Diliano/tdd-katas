from katas.longest_consecutive_sequence.longest_consecutive_sequence import (
    longest_consecutive_sequence,
)


def test_handles_empty_input():
    # Arrange
    test_input = []
    expected = 0
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected


def test_handles_input_with_one_num():
    # Arrange
    test_input = [5]
    expected = 1
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected


def test_handles_input_with_no_consecutive_sequence():
    # Arrange
    test_input = [10, 20, 30]
    expected = 1
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected


def test_calculates_length_of_consecutive_sequence():
    # Arrange
    test_input = [10, 5, 12, 3, 55, 11]
    expected = 3
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = [100, 4, 200, 1, 3, 2]
    expected = 4
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected
