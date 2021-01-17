import random
from typing import Dict, List, Tuple
from tictactoe.board import Board, Winner

class Node():
    def __init__(self, board: Board, move: List = None, depth: int = 0) -> None:
        self.board = board
        self.move = move
        self.children = []
        self.depth = depth
    
    def build_tree(self, max_depth: int):
        if self.depth < max_depth:
            for move in self.board.find_feasible_moves():
                child = Node(self.board.apply_move(move[0], move[1]), move, self.depth + 1)
                child.build_tree(max_depth)
                self.children.append(child)

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
    """Random search algorithm. It will select a move in a complete random manner.
    """
    def __init__(self) -> None:
        super().__init__("Random")
    
    def search(self, board: Board) -> Board:
        feasible_moves = board.find_feasible_moves()
        move = feasible_moves[random.randrange(0, len(feasible_moves))]
        return board.apply_move(move[0], move[1])

class Minimax(SearchAlgorithm):
    """Minimax search algorithm.
    """
    def __init__(self, player: bool, depth: int) -> None:
        super().__init__("Minimax")
        self.player = player
        self.depth = depth

    def _evaluate(self, board: Board) -> float:
        """Returns the score of the board.

        Args:
            board (Board): board to evaluate

        Returns:
            float: score of the board from the player' perspective.
        """
        if board.winner == Winner.UNDETERMINED or board.winner == Winner.DRAW:
            return 0

        if (self.player):
            return 1 if board.winner == Winner.X else -1
            
        return 1 if board.winner == Winner.O else -1

    def _evaluate_node(self, node: Node):
        # If it is a node at the bottom
        if node.depth == self.depth or len(node.children) == 0:
            score = self._evaluate(node.board)
            node.score = score if self.player else -score
            return
        
        # If it is an intermediate node
        minimax = None
        for child in node.children:
            self._evaluate_node(child)
            
            # Our turn
            if node.board.next == self.player:
                if minimax == None or child.score > minimax:
                    minimax = child.score

            # Opponent turn
            else:
                if minimax == None or child.score < minimax:
                    minimax = child.score

        node.score = minimax


    def search(self, board: Board) -> Board:
        node = Node(board)
        node.build_tree(self.depth)
        max = None
        chosen = None
        for child in node.children:
            self._evaluate_node(child)
            if max == None or child.score > max:
                max = child.score
                chosen = child
        
        return chosen.board

