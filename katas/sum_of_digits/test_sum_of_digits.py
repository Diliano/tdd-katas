from katas.sum_of_digits.sum_of_digits import sum_of_digits


def test_handles_input_of_zero():
    # Arrange
    test_input = 0
    expected = 0
    # Act
    result = sum_of_digits(test_input)
    # Assert
    assert result == expected
