import itertools
import os
from typing import List, Optional


def main():
    game = GameOfLife(4, 3)
    game.init_state(
        [1, 1, 0],
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1],
    )
    game.run()


Board = List[List[int]]


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
        r = ''
        for row in self.board:
            for cell in row:
                r += 'X' if cell == 1 else ' '
            r += os.linesep
        return r

    def step(self) -> None:
        new_board = [[0] * self.cols for _ in range(self.rows)]
        for i, row in enumerate(self.board):
            new_board[i] = [self.step_cell(self.board, i, j)
                            for j, _ in enumerate(row)]

    @staticmethod
    def step_cell(board: Board, i: int, j: int) -> bool:
        return True

    def run(self, steps: Optional[int] = None) -> None:
        for _ in range(steps) if steps is not None else itertools.count():
            self.step()
            print(self)


if __name__ == '__main__':
    main()
