import unittest
import numpy as np
import tictactoe.board as board

class TestBoard(unittest.TestCase):

    def test_init(self):

        # Check empty
        b = board.Board([[None, None, None], [None, None, None], [None, None, None]], 0)
        self.assertIsNone(b.winner)

        # Check row
        b = board.Board([[None, False, True], [True, False, True], [None, False, None]], 6)
        self.assertFalse(b.winner)

        # Check column
        b = board.Board([[True, False, None], [True, False, True], [True, None, False]], 7)
        self.assertTrue(b.winner)

        # Check [0,0] to [n,n] diagonal
        b = board.Board([[False, True, None], [True, False, True], [None, None, False]], 6)
        self.assertFalse(b.winner)

        # Check [0,n] to [n,0] diagonal
        b = board.Board([[None, None, True], [False, True, False], [True, None, None]], 5)
        self.assertTrue(b.winner)

        # Check no winner
        b = board.Board([[None, True, None], [False, True, False], [True, None, False]], 6)
        self.assertIsNone(b.winner)

    
