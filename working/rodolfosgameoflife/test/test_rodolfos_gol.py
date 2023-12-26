"""Test for my implementation of the Game of Life."""

from mymodule import GameOfLife

import pytest
import numpy as np


@pytest.fixture
def game():
    """Return a game object."""
    return GameOfLife()


def test_init(game):
    assert game.rows == 6
    assert game.cols == 4
    matrix = getattr(game, "matrix")
    assert isinstance(matrix, np.ndarray)


def test_init_random(game):
    game.init_random()
    assert isinstance(game.matrix, np.ndarray)


def test_neighbours(game):
    game.matrix = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0]])
    expected = np.array([[1, 1, 1], [3, 2, 2], [2, 2, 2]])

    nb = game.get_neighbours()
    assert (nb == expected).all()


def test_next(game):
    game.matrix = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0]])
    expected = np.array([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
    game.next()
    assert (game.matrix == expected).all()
