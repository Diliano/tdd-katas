from katas.convert_to_upper_camel_case.to_upper_camel_case import to_upper_camel_case


def test_handles_empty_input():
    # Arrange
    test_input = ""
    expected = ""
    # Act
    result = to_upper_camel_case(test_input)
    # Assert
    assert result == expected
