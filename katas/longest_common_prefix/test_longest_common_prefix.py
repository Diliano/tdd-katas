from katas.longest_common_prefix.longest_common_prefix import longest_common_prefix


def test_handles_empty_input():
    # Arrange
    test_input = []
    expected = ""
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected


def test_handles_only_one_input_str():
    # Arrange
    test_input = ["hello"]
    expected = "hello"
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected


def test_finds_longest_common_prefix():
    # Arrange
    test_input = ["flower", "flow", "flight"]
    expected = "fl"
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = ["interview", "internet", "internal"]
    expected = "inter"
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected

    # Arrange
    test_input = ["apple", "ape", "april"]
    expected = "ap"
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected


def test_handles_input_with_no_common_prefix():
    # Arrange
    test_input = ["dog", "racecar", "car"]
    expected = ""
    # Act
    result = longest_common_prefix(test_input)
    # Assert
    assert result == expected
