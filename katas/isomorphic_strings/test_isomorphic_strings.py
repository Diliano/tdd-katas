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


def test_identifies_isomorphic_strings():
    # Arrange
    test_input = ("egg", "add")
    expected = True
    # Act
    result = is_isomorphic(*test_input)
    # Assert
    assert result is expected

    # Arrange
    test_input = ("paper", "title")
    expected = True
    # Act
    result = is_isomorphic(*test_input)
    # Assert
    assert result is expected


def test_identifies_non_isomorphic_strings():
    # Arrange
    test_input = ("foo", "bar")
    expected = False
    # Act
    result = is_isomorphic(*test_input)
    # Assert
    assert result is expected

    # Arrange
    test_input = ("ab", "aa")
    expected = False
    # Act
    result = is_isomorphic(*test_input)
    # Assert
    assert result is expected
