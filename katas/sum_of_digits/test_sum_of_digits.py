from katas.sum_of_digits.sum_of_digits import sum_of_digits


def test_handles_input_of_zero():
    # Arrange
    test_input = 0
    expected = 0
    # Act
    result = sum_of_digits(test_input)
    # Assert
    assert result == expected


def test_handles_single_digit_input():
    # Arrange
    test_input = 5
    expected = 5
    # Act
    result = sum_of_digits(test_input)
    # Assert
    assert result == expected


def test_calculates_sum_of_digits():
    # Arrange
    test_input = 123
    expected = 6
    # Act
    result = sum_of_digits(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = 456
    expected = 15
    # Act
    result = sum_of_digits(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = 98765
    expected = 35
    # Act
    result = sum_of_digits(test_input)
    # Assert
    assert result == expected
