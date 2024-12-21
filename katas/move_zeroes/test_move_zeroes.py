from katas.move_zeroes.move_zeroes import move_zeroes


def test_handles_empty_input():
    # Arrange
    test_input = []
    expected = []
    # Act
    result = move_zeroes(test_input)
    # Assert
    assert result == expected


def test_handles_list_with_no_zeroes():
    # Arrange
    test_input = [1, 2, 3]
    expected = [1, 2, 3]
    # Act
    result = move_zeroes(test_input)
    # Assert
    assert result == expected


def test_handles_list_with_only_zeroes():
    # Arrange
    test_input = [0, 0, 0]
    expected = [0, 0, 0]
    # Act
    result = move_zeroes(test_input)
    # Assert
    assert result == expected
