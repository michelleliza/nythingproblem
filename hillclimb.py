import board as b
import copy

class HillClimbing():
    def __init__(self, listPawn):
        #initial config
        self.board = b.Board(listPawn)
        self.board.initPawn()
        stop = False

        while not stop:
            currentCost = self.board.cost()
            tempBoard = copy.deepcopy(self.board)
            minCost = currentCost
            for pawn in tempBoard.listPawn:
                for i in range(0,8):
                    for j in range(0,8):
                        found = False
                        for pawn2 in tempBoard.listPawn:
                            if i == pawn2.x and j == pawn2.y:
                                found = True
                        if not found:
                            pawn.x = i
                            pawn.y = j
                            newCost = tempBoard.cost()
                            if newCost < minCost:
                                minCost = newCost
                                self.board = copy.deepcopy(tempBoard)
            if minCost == currentCost: #stuck
                stop = True #stop searching 