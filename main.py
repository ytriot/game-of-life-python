import itertools
import os
from time import sleep
from typing import List, Optional, Generator


def main():
    game = GameOfLife(20, 20)
    game.init_state(
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    )
    for _ in game.run():
        clear()
        print(game)
        sleep(0.01)

class GameOfLife:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols for _ in range(rows)]

    def init_state(self, *rows: List[int]) -> None:
        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                self.board[i][j] = cell

    def __str__(self) -> str:
        r = ' ' + '--' * self.cols + '\n'
        for row in self.board:
            r += '|' + ''.join('[]' if cell == 1 else '  '
                               for cell in row) + '|\n'
        r += ' ' + '--' * self.cols
        return r

    def step(self) -> None:
        new_board = [[0] * self.cols for _ in range(self.rows)]
        for i, row in enumerate(self.board):
            new_board[i] = [self._step_cell(i, j) for j, _ in enumerate(row)]
        self.board = new_board

    def _step_cell(self, i: int, j: int) -> int:
        alive_neighbors = sum(self._neighbors(i, j))
        return self.board[i][j] if alive_neighbors == 2 else int(alive_neighbors == 3)

    def _neighbors(self, i: int, j: int) -> List[int]:
        return [self.board[(i + dy) % self.rows][(j + dx) % self.cols]
                for dx in [-1, 0, 1]
                for dy in [-1, 0, 1]
                if dx != 0 or dy != 0]

    def run(self, steps: Optional[int] = None) -> Generator[int, None, None]:
        for i in range(steps) if steps is not None else itertools.count():
            self.step()
            yield i


def clear():
    # CrOsS- pLaTfOrM ;)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
