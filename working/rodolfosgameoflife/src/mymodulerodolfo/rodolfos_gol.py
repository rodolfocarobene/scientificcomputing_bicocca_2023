"""Rodolfo's Game Of Life.

(Obviously Conway's)
"""
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

plt.ioff()
plt.rcParams["animation.html"] = "jshtml"
plt.rcParams["figure.dpi"] = 150


class GameOfLife:
    """Main class."""

    def __init__(self, rows=6, cols=4):
        """Initilize setting empty matrix."""
        self.rows = rows
        self.cols = cols
        self.matrix = np.zeros((rows, cols), dtype=np.int32)

    def init_random(self):
        """Random start, since otherwise is a bit of a pain."""
        self.matrix = np.random.choice([0, 1], size=(self.rows, self.cols))

    def get_neighbours(self):
        """Return matrix of neighbors."""
        c = np.pad(self.matrix, 1)
        neighbours = np.zeros(c.shape, dtype=np.int32)

        for dir, ax in product((-1, 1), (0, 1)):
            """neighbors up-down-left-right"""
            neighbours = neighbours + np.roll(c, dir, axis=ax)

        for dir1, dir2 in product((1, -1), (1, -1)):
            """neighbors in diagonal directions"""
            neighbours = neighbours + np.roll(np.roll(c, dir1, axis=1), dir2, axis=0)

        return np.array([row[1:-1] for row in neighbours[1:-1]])

    def next(self):
        """Rules.

        - any live cell with two or three live neighbors survives
        - any dead cell with three live neighbors becomes a live cell
        - all other live cells die in the next generation. All other dead cells stay dead
        """
        next = self.matrix.copy()

        alive = self.matrix == 1
        dead = self.matrix == 0

        neighbours = self.get_neighbours()

        m = np.logical_or(neighbours > 3, neighbours < 2)
        n = neighbours == 3

        new_dead = np.logical_and(m, alive)
        new_alive = np.logical_and(n, dead)

        next[new_dead] = 0
        next[new_alive] = 1

        self.matrix = next

    def show_and_next(self, _):
        """Use for animations."""
        plt.imshow(self.matrix)
        self.next()
