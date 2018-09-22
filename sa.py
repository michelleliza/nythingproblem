from random import randint, uniform
import board as b
import copy
import math

def printListPawn(listPawn) :
    for pawn in listPawn:
        if isinstance(pawn, b.Queen):
            print('Q', end=' ')
        elif isinstance(pawn, b.Bishop):
            print('B', end=' ')
        elif isinstance(pawn, b.Rook):
            print('R', end=' ')
        elif isinstance(pawn, b.Knight):
            print('K', end=' ')
        print(pawn.x, end=' ')
        print(pawn.y, end='\n')

class SimulatedAnnealing() :
    def __init__(self, listPawn) :
        # initial config
        self.board = b.Board(listPawn)
        oldCost = self.board.cost()
        self.t = 1000
        self.alpha = 0.9
        count = 0 # count is used for halt.
        halt = 5000 # halt when n iteration doesn't get new solution (stuck)
        decrease = 50 # temp decrease after n iteration
        while count < halt :
            for i in range (0, decrease) :
                # do random move and get new solution (temp)
                newBoard = self.newSolutionSA()
                newCost = newBoard.cost()
                ap = self.boltzman(oldCost, newCost)
                
                # if new cost < old cost the value of ap always > 1
                if ap >= uniform(0, 1) :
                    self.board = newBoard
                    oldCost = newCost

                    # add count if oldCost == newCost
                    if oldCost == newCost :
                        count += 1
                    else :
                        count = 0
                else :
                    count += 1

            self.t *= self.alpha
        
    def newSolutionSA(self) :
        while True :
            n = randint(0, len(self.board.listPawn) - 1)
            x = randint(0, 7)
            y = randint(0, 7)
            found = False

            for pawn in self.board.listPawn :
                if (pawn.x == x and pawn.y == y) :
                    found = True
                    break

            if not found :
                newBoard = copy.deepcopy(self.board)
                newBoard.listPawn[n].x = x
                newBoard.listPawn[n].y = y
                return newBoard

    def boltzman(self, oldCost, newCost) :
        return math.exp(-(newCost - oldCost)/self.t)