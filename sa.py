from random import randint, uniform
import board as b
import copy
import math

class SimulatedAnnealing() :
    def __init__(self, listPawn) :
        # initial config
        self.board = b.Board(listPawn)
        oldCost = self.board.cost()

        # initial temperature
        self.t = 1000 
        # temperature gradually decrease by alpha
        self.alpha = 0.9 
        # count is used for halt
        count = 0 
        # halt when n iteration doesn't get new solution (stuck) or get the same cost with new solution
        halt = 500 
        # temperature decrease after n iteration
        decrease = 50
        while count < halt :
            for i in range (0, decrease) :
                # do random move and get new solution (temp)
                newBoard = self.newSolutionSA()
                # calculate new cost
                newCost = newBoard.cost()
                
                if newCost < oldCost :
                    # accept the solution because new solution is "good" moves
                    # change the current solution to the new solution
                    self.board = newBoard
                    oldCost = newCost
                else :
                    # accept the solution ("bad" moves) only with probability
                    # acceptance probabilty
                    ap = self.boltzman(oldCost, newCost)

                    if ap > uniform(0, 1) :
                        # change the current solution to the new solution
                        self.board = newBoard
                        
                        # add count if oldCost == newCost
                        if oldCost == newCost :
                            count += 1
                        else :
                            count = 0

                        oldCost = newCost

                    else :
                        # keep the current solution
                        count += 1
                
                if newCost == 0 :
                    # halt when cost is already 0 (global minima)
                    return

            self.t *= self.alpha
        
    def newSolutionSA(self) :
    # do random move to get new solution
        while True :
            n = randint(0, len(self.board.listPawn) - 1)
            x = randint(0, 7)
            y = randint(0, 7)
            found = False

            # make sure the new x and y is empty
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
    # calculate acceptance probabilty with boltzman distribution
        try:
            return math.exp(-(newCost - oldCost)/self.t)
        except OverflowError:
            # overflow when temperature too low (limit approaching 0)
            if newCost == oldCost :
                # return 1 because exp(0) is 1
                return 1
            # newCost > oldCost
            return 0