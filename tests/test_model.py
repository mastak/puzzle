import pytest

from puzzle.constants import Direction
from puzzle.exceptions import IncorrectMoveError
from puzzle.models import PuzzleData


def test_move_position():
    puzzle = PuzzleData()
    puzzle._current_state = puzzle._success_state
    assert puzzle.is_success
    assert puzzle.current_value == 1

    puzzle.move_position(Direction.right)
    assert puzzle.current_value == 2

    puzzle.move_position(Direction.down)
    assert puzzle.current_value == 6

    puzzle.move_position(Direction.left)
    assert puzzle.current_value == 5

    with pytest.raises(IncorrectMoveError) as exc:
        puzzle.move_position(Direction.left)
    assert "Сell 2:0 unavailable" in str(exc.value)


def test_move_tiles():
    puzzle = PuzzleData()
    puzzle._current_state = puzzle._success_state
    assert puzzle._current_state == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0],
    ]

    with pytest.raises(IncorrectMoveError) as exc:
        puzzle.move_tiles(Direction.right)
    assert "Сell 1:2 is not empty" in str(exc.value)

    puzzle._current_row, puzzle._current_col = 3, 2
    assert puzzle.current_value == 15

    puzzle.move_tiles(Direction.right)
    assert puzzle.current_value == 15
    assert puzzle._current_row == 3
    assert puzzle._current_col == 3
    assert puzzle._current_state == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 0, 15],
    ]
