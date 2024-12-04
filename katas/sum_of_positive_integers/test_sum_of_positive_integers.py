from katas.sum_of_positive_integers.sum_of_positive_integers import (
    sum_of_positive_integers,
)


def test_handles_empty_input():
    # Arrange
    test_input = []
    expected = 0
    # Act
    result = sum_of_positive_integers(test_input)
    # Assert
    assert result == expected


def test_handles_all_negative_numbers():
    # Arrange
    test_input = [-1, -2, -3, -4, -5]
    expected = 0
    # Act
    result = sum_of_positive_integers(test_input)
    # Assert
    assert result == expected


def test_sums_all_positive_numbers():
    # Arrange
    test_input = [1, 2, 3, 4, 5]
    expected = 15
    # Act
    result = sum_of_positive_integers(test_input)
    # Assert
    assert result == expected
