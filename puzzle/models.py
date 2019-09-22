import random
import typing as t

from puzzle.constants import Direction
from puzzle.exceptions import IncorrectMoveError
from puzzle.utils import make_state

EMPTY_SYMBOL = 0


class PuzzleData:
    def __init__(self, size=4):
        self._size = size
        alphabet = list(range(1, size * size))
        alphabet.append(EMPTY_SYMBOL)
        self._success_state = make_state(alphabet)
        random.shuffle(alphabet)
        self._current_state = make_state(alphabet)
        self._current_row = 0
        self._current_col = 0

    @property
    def is_success(self) -> bool:
        return self._current_state == self._success_state

    @property
    def current_value(self) -> int:
        return self._current_state[self._current_row][self._current_col]

    @property
    def current_state(self) -> t.List[t.List[int]]:
        return self._current_state

    def move_position(self, direction: Direction):
        self._current_row, self._current_col = self._get_next_position(direction)

    def move_tiles(self, direction: Direction):
        new_row, new_col = self._get_next_position(direction)
        new_value = self._current_state[new_row][new_col]

        if new_value != EMPTY_SYMBOL:
            raise IncorrectMoveError(f'Сell {new_row + 1}:{new_col + 1} '
                                     f'is not empty')

        current_value = self._current_state[self._current_row][self._current_col]
        self._current_state[new_row][new_col] = current_value
        self._current_state[self._current_row][self._current_col] = EMPTY_SYMBOL
        self._current_row, self._current_col = new_row, new_col

    def _get_next_position(self, direction: Direction) -> t.Tuple[int, int]:
        delta_row, delta_col = {
            Direction.up: (-1, 0),
            Direction.down: (1, 0),
            Direction.right: (0, 1),
            Direction.left: (0, -1),
        }[direction]
        new_row = self._current_row + delta_row
        new_col = self._current_col + delta_col
        if 0 <= new_row < self._size and 0 <= new_col < self._size:
            return new_row, new_col
        raise IncorrectMoveError(f'Сell {new_row + 1}:{new_col + 1} unavailable')
