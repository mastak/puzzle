import pytest
from puzzle.utils import make_state


def test_make_state():
    assert make_state([1, 2, 3, 4]) == [[1, 2], [3, 4]]
    assert make_state([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]


def test_make_state_validation():
    with pytest.raises(ValueError) as exc:
        make_state([1, 2, 3, 4, 5])
    assert "The length of the alphabet has no integer square root" == str(exc.value)
