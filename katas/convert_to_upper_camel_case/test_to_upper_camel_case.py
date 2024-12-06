from katas.convert_to_upper_camel_case.to_upper_camel_case import to_upper_camel_case


def test_handles_empty_input():
    # Arrange
    test_input = ""
    expected = ""
    # Act
    result = to_upper_camel_case(test_input)
    # Assert
    assert result == expected


def test_handles_input_with_only_spaces():
    # Arrange
    test_input = "    "
    expected = ""
    # Act
    result = to_upper_camel_case(test_input)
    # Assert
    assert result == expected


def test_capitalises_first_letter_given_single_word():
    # Arrange
    test_input = "python"
    expected = "Python"
    # Act
    result = to_upper_camel_case(test_input)
    # Assert
    assert result == expected
