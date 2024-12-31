from katas.isomorphic_strings.isomorphic_strings import is_isomorphic


def test_handles_empty_strings():
    # Arrange
    test_input = ("", "")
    expected = True
    # Act
    result = is_isomorphic(*test_input)
    # Assert
    assert result is expected


def test_handles_strings_of_different_lengths():
    # Arrange
    test_input = ("hi", "bye")
    expected = False
    # Act
    result = is_isomorphic(*test_input)
    # Assert
    assert result is expected
