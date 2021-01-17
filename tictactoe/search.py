import random
from tictactoe.board import Board

class SearchAlgorithm():
    """Base class for a search algorithm.
    """
    def __init__(self, name: str) -> None:
        self.name = name
    
    def search(self, board: Board) -> Board:
        """Searches and returns the next move.

        Args:
            board (Board): current board.

        Returns:
            Board: board after the selected move, or None if there are no feasible moves.
        """
        pass

class Random(SearchAlgorithm):
    def __init__(self) -> None:
        super().__init__("Random")
    
    def search(self, board: Board) -> Board:
        feasible_moves = board.find_feasible_moves()
        move = feasible_moves[random.randrange(0, len(feasible_moves))]
        return board.apply_move(move[0], move[1])