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
