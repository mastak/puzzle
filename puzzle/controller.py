from puzzle.models import PuzzleData
from puzzle.views import PuzzleView
from puzzle.constants import Direction
from puzzle.exceptions import IncorrectMoveError


HELP_STR = '''
→↑↓← - move position
a s d w - move selected tile
q - exit
'''

CODE_A = ord('a')
CODE_W = ord('w')
CODE_S = ord('s')
CODE_D = ord('d')


def game_runner():
    puzzle = PuzzleData()
    viewer = PuzzleView(HELP_STR)
    try:
        while True:
            view_frame(puzzle, viewer)
    except KeyboardInterrupt:
        pass
    finally:
        viewer.close()


def view_frame(puzzle, viewer):
    try:
        char = viewer.view_board(puzzle)
        if char == ord('q'):
            exit()

        if 258 <= char <= 261:
            direction = {
                258: Direction.down,
                259: Direction.up,
                260: Direction.left,
                261: Direction.right,
            }[char]
            puzzle.move_position(direction)

        elif char in {CODE_A, CODE_W, CODE_S, CODE_D}:
            direction = {
                CODE_S: Direction.down,
                CODE_W: Direction.up,
                CODE_A: Direction.left,
                CODE_D: Direction.right,
            }[char]
            puzzle.move_tiles(direction)
        else:
            viewer.print_text(f'no command for key {char}')
    except IncorrectMoveError as exc:
        viewer.print_text(f'{str(exc)}')
