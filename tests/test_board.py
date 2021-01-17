import unittest
import numpy as np
import tictactoe.board as board

class TestBoard(unittest.TestCase):

    def test_init(self):
        # Check empty
        b = board.Board([[None, None, None], [None, None, None], [None, None, None]], 0)
        self.assertEqual(0, b.moves)
        self.assertEqual(True, b.next)
        self.assertIsNone(b.winner)
        
        # Check row
        b = board.Board([[None, False, True], [True, False, True], [None, False, None]], 6)
        self.assertEqual(6, b.moves)
        self.assertEqual(True, b.next)
        self.assertFalse(b.winner)

        # Check column
        b = board.Board([[True, False, None], [True, False, True], [True, None, False]], 7)
        self.assertEqual(7, b.moves)
        self.assertEqual(False, b.next)
        self.assertTrue(b.winner)

        # Check [0,0] to [n,n] diagonal
        b = board.Board([[False, True, None], [True, False, True], [None, None, False]], 6)
        self.assertEqual(6, b.moves)
        self.assertEqual(True, b.next)
        self.assertFalse(b.winner)

        # Check [0,n] to [n,0] diagonal
        b = board.Board([[None, None, True], [False, True, False], [True, None, None]], 5)
        self.assertEqual(5, b.moves)
        self.assertEqual(False, b.next)
        self.assertTrue(b.winner)

        # Check no winner
        b = board.Board([[None, True, None], [False, True, False], [True, None, False]], 6)
        self.assertEqual(6, b.moves)
        self.assertEqual(True, b.next)
        self.assertIsNone(b.winner)

    def test_apply_move(self):
        b = board.Board([[None, None, None], [None, None, None], [None, None, None]], 0)
        
        b = b.apply_move(0, 0)
        np.testing.assert_array_equal([[True, None, None], [None, None, None], [None, None, None]], b.state)
        self.assertEqual(1, b.moves)
        self.assertEqual(False, b.next)

        b = b.apply_move(1, 1)
        np.testing.assert_array_equal([[True, None, None], [None, False, None], [None, None, None]], b.state)
        self.assertEqual(2, b.moves)
        self.assertEqual(True, b.next)
        self.assertIsNone(b.winner)

        b = b.apply_move(0, 1)
        np.testing.assert_array_equal([[True, True, None], [None, False, None], [None, None, None]], b.state)
        self.assertEqual(3, b.moves)
        self.assertEqual(False, b.next)
        self.assertIsNone(b.winner)

        b = b.apply_move(2, 2)
        np.testing.assert_array_equal([[True, True, None], [None, False, None], [None, None, False]], b.state)
        self.assertEqual(4, b.moves)
        self.assertEqual(True, b.next)
        self.assertIsNone(b.winner)

        b = b.apply_move(0, 2)
        np.testing.assert_array_equal([[True, True, True], [None, False, None], [None, None, False]], b.state)
        self.assertEqual(5, b.moves)
        self.assertEqual(False, b.next)
        self.assertEqual(True, b.winner)
    
    def test_str(self):
        b = board.Board([[None, None, None], [None, None, None], [None, None, None]], 0)
        self.assertEqual(" -  -  - \n" + " -  -  - \n" + " -  -  - \n", str(b))

        b = b.apply_move(0, 0)
        self.assertEqual(" -  -  - \n" + " -  -  - \n" + " X  -  - \n", str(b))

        b = b.apply_move(0, 2)
        self.assertEqual(" O  -  - \n" + " -  -  - \n" + " X  -  - \n", str(b))

        b = b.apply_move(1, 0)
        self.assertEqual(" O  -  - \n" + " -  -  - \n" + " X  X  - \n", str(b))