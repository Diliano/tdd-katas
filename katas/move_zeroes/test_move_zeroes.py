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


def test_moves_one_zero():
    # Arrange
    test_input = [0, 1, 2]
    expected = [1, 2, 0]
    # Act
    result = move_zeroes(test_input)
    # Assert
    assert result == expected


def test_moves_multiple_zeroes():
    # Arrange
    test_input = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    # Act
    result = move_zeroes(test_input)
    # Assert
    assert result == expected
