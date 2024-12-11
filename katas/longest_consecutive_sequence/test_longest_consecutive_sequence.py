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


def test_handles_input_with_multiple_consecutive_sequences():
    # Arrange
    test_input = [1, 2, 11, 9, 10, 4, 3, 20, 15]
    expected = 4
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = [100, 101, 102, 97, 96, 45, 44]
    expected = 3
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected


def test_handles_input_list_duplicates():
    # Arrange
    test_input = [1, 2, 0, 1]
    expected = 3
    # Act
    result = longest_consecutive_sequence(test_input)
    # Assert
    assert result == expected
