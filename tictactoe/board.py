from typing import List
from enum import Enum
import numpy as np

class Winner(Enum):
    UNDETERMINED = 1
    X = 2
    O = 3
    DRAW = 4

class Board:
    """Tic-tac-toe board representation.

    Attributes:
        state (2D-array): State of the board represented by True (X)/False (O) flags.
        moves (int): Number of moves taken so far.
        next (bool): Flag indicating the next player, True (X) or False (O).
        winner (Winner): indicates the winner.
    """
    def __init__(self, state = [[None, None, None], [None, None, None], [None, None, None]], moves: int = 0) -> None:
        """Constructor. It should only be used externally to spawn a brand-new board state, i.e. calling it
        with no arguments. Arguments are meant to be used internally when creating a new instnace after applying
        a move to an existing one.

        Args:
            state (list, optional): board state. Defaults to [[None, None, None], [None, None, None], [None, None, None]].
            moves (int, optional): number of moves taken so fare (this could be computed based on the number of non empty squares,
            but it is left as an argument to avoid looping over the state every time a move is applied). Defaults to 0.
        """
        self.state = state
        self.moves = moves
        self.next = moves % 2 == 0
        size = len(state)

        # Check only if the number of moves made reaches the minimum for a winning position.
        if self.moves >= (2*size -1):
            self.winner = self._determine_winner()
        else:
            self.winner = Winner.UNDETERMINED

    def _determine_winner(self) -> Winner:
        size = len(self.state)

        # Check columns
        for i in range(size)         :
            ref = None
            for j in range(size):
                s = self.state[i][j]
                # Square is empty
                if s == None:
                    break
                # First square, set reference
                if ref == None:
                    ref = s
                else:
                    # Subsequent square does not match reference
                    if s != ref:
                        break
                    # All squares have matched the reference
                    if j == size-1:
                        return Winner.X if ref else Winner.O

        # Check rows
        for j in range(size):
            ref = None
            for i in range(size):
                s = self.state[i][j]
                # Square is empty
                if s == None:
                    break
                # First square, set reference
                if ref == None:
                    ref = s
                else:
                    # Subsequent square does not match reference
                    if s != ref:
                        break
                    # All squares have matched the reference
                    if i == size-1:
                        return Winner.X if ref else Winner.O
        
        # Check [0,0] to [n,n] diagonal
        ref = None
        for i in range(size):
            s = self.state[i][i]            
            # Square is empty
            if s == None:
                break
            # First square, set reference
            if ref == None:
                ref = s
            else:
                # Subsequent square does not match reference
                if s != ref:
                    break
                # All squares have matched the reference
                if i == size-1:
                    return Winner.X if ref else Winner.O
        
        # Check [0,n] to [n,0] diagonal
        ref = None
        for i in range(size):
            s = self.state[i][size-1-i]            
            # Square is empty
            if s == None:
                break
            # First square, set reference
            if ref == None:
                ref = s
            else:
                # Subsequent square does not match reference
                if s != ref:
                    break
                # All squares have matched the reference
                if i == size-1:
                    return Winner.X if ref else Winner.O
        
        if self.moves == size * size:
            return Winner.DRAW
        
        return Winner.UNDETERMINED

    def apply_move(self, i: int, j: int) -> 'Board':
        """Applies the given move to the instance.

        Returns:
            Board: a new instance of the board with the applied move.
        """
        copy = np.copy(self.state)
        copy[i,j] = self.next
        return Board(copy, self.moves+1)

    def find_feasible_moves(self) -> List:
        """Finds all feasible moves (depth 1)

        Returns:
            List: a list containing the coordinates of all feasible moves.
        """
        if self.winner == Winner.UNDETERMINED:
            size = len(self.state)
            feasible = []
            for i in range(size):
                for j in range(size):
                    if self.state[i][j] == None:
                        feasible.append([i, j])
            return feasible           

        return []

    def __str__(self) -> str:
        """Returns a string representing the status of the board.

        An additional line-break is appended to the returned string. Example:

         X O - 
         X - O 
         O - X 

        Returns:
            str: string-based representation of the board status.
        """
        size = len(self.state)
        s = ''
        for j in range(size):
            for i in range(size):
                square = self.state[i][size-1-j]
                if square == None:
                    s += ' - '
                else:
                    if square:
                        s += ' X '
                    else:
                        s += ' O '
            s += '\n'
        return s
