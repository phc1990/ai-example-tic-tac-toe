from unittest.main import main
from tictactoe import search
from tictactoe.search import Minimax, Node, SearchAlgorithm, Random
from tictactoe.board import Board, Winner

def app(algorithm: SearchAlgorithm, player: bool):

    b = Board()
    if not player:
        print(str(b))

    while b.winner == Winner.UNDETERMINED:
        
        if b.next == player:
            b = algorithm.search(b)
            print("\n")
            print(str(b))
        else:
            print("Your move:")
            i = int(input("Enter X coorinate..."))
            j = int(input("Enter Y coordinate..."))
            b = b.apply_move(i, j)

    s = "DRAW"
    if b.winner == Winner.X:
        s = "I WON" if player else "YOU WON"
    elif b.winner == Winner.O:
        s = "YOU WON" if player else "I WON"

    print("**** " + s + " ****")


if __name__ == "__main__":
    app(Minimax(True, 5), True)