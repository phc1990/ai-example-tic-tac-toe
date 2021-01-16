import numpy as np

class Board:
    """Tic-tac-toe board representation.

    Attributes:
        state (2D-array): State of the board represented by True (X)/False (O) flags.
        moves (int): Number of moves taken so far.
        next (bool): Flag indicating the next player, True (X) or False (O).
        winner (bool): Flag indicating the winner, True (X), False (O) or None (no winner).
    """
    def __init__(self, state = [[None, None, None], [None, None, None], [None, None, None]], moves: int = 0) -> None:
        self.state = state
        self.moves = moves
        self.next = moves % 2 == 0
        size = len(state)

        # Check only if the number of moves made reaches the minimum for a winning position.
        if self.moves >= (2*size -1):
            self.winner = self.determine_winner()
        else:
            self.winner = None

    def determine_winner(self) -> bool:
        size = len(self.state)

        # Check columns
        for i in range(size):
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
                        return ref
        
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
                        return ref
        
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
                    return ref
        
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
                    return ref

    def apply_move(self, i: int, j: int) -> 'Board':
        copy = np.copy(self.state)
        copy[i,j] = self.next
        return Board(copy, self.moves+1)

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
