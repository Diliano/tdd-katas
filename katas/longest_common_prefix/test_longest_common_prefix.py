from katas.longest_common_prefix.longest_common_prefix import longest_common_prefix


def test_handles_empty_input():
    # Arrange
    test_input = []
    expected = []
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected
