import curses as curses
from puzzle.models import PuzzleData


class PuzzleView:
    def __init__(self, help_str: str):
        self._screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self._screen.keypad(1)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.curs_set(0)
        self.print_help(help_str)
        self.board = self._screen.derwin(14, 26, 0, 0)
        self.msg_box = self._screen.derwin(1, 26, 15, 0)
        self.board.box()

    def close(self):
        self._screen.erase()
        self._screen.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def view_board(self, puzzle: PuzzleData):
        self.board.erase()
        self.board.box()
        self.board.refresh()

        tiles = []
        tile_width = 6
        tile_height = 3
        for i in range(4):
            for j in range(4):
                tile = self.board.derwin(tile_height, tile_width,
                                         i * tile_height + 1,
                                         j * tile_width + 1)
                tile.box()

                value = puzzle.current_state[i][j]
                if value == puzzle.current_value:
                    attr = curses.A_UNDERLINE | curses.A_BOLD
                else:
                    attr = curses.A_NORMAL
                tile.addstr(1, 2, f'{value}', attr)
                tile.refresh()
                tiles.append(tile)
        return self._screen.getch()

    def print_text(self, text):
        self.msg_box.erase()
        self.msg_box.addstr(0, 0, text)
        self.msg_box.refresh()

    def print_help(self, text):
        self._screen.addstr(16, 20, text)
        self._screen.refresh()
