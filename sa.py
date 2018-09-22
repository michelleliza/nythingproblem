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
        halt = 5000 
        # temperature decrease after n iteration
        decrease = 50
        while count < halt :
            for i in range (0, decrease) :
                if oldCost == 0 :
                    # stop iteration when hit cost already 0
                    return
                # do random move and get new solution (temp)
                newBoard = self.newSolutionSA()
                # calculate new cost
                newCost = newBoard.cost()
                # acceptance probabilty
                ap = self.boltzman(oldCost, newCost)
                
                # if new cost < old cost the value of ap always > 1
                if ap >= uniform(0, 1) :
                    # change the current solution to the new solution
                    self.board = newBoard
                    oldCost = newCost

                    # add count if oldCost == newCost
                    if oldCost == newCost :
                        count += 1
                    else :
                        count = 0
                else :
                    # keep the current solution
                    count += 1

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
            # overflow when temperature too low so (limit approaching 0)
            return 0