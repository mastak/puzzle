import math
import typing as t


def make_state(alphabet: t.List[any]):
    size = int(math.sqrt(len(alphabet)))
    if size * size != len(alphabet):
        raise ValueError('The length of the alphabet has no integer square root')

    return [[alphabet[j + i * size] for j in range(size)] for i in range(size)]
