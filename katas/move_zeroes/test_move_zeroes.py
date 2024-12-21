from katas.move_zeroes.move_zeroes import move_zeroes


def test_handles_empty_input():
    # Arrange
    test_input = []
    expected = []
    # Act
    result = move_zeroes(test_input)
    # Assert
    assert result == expected
