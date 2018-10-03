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
            tempBoard = copy.deepcopy(self.board) #new board to move pawns
            minCost = currentCost
            for pawn in tempBoard.listPawn:
                maxHit = 0
                minHit = 100
                for i in range(0,8):
                    for j in range(0,8):
                        found = False
                        for pawn2 in tempBoard.listPawn:
                            if i == pawn2.x and j == pawn2.y:
                                found = True
                        if not found: #no conflicting pawns
                            pawn.x = i
                            pawn.y = j
                            newCost = tempBoard.cost()
                            if newCost < minCost: #climbing
                                minCost = newCost
                                self.board = copy.deepcopy(tempBoard)
                            elif newCost == minCost:
                                crtHitSame, crtHitDiff = pawn.hit(tempBoard.listPawn)
                                if crtHitSame > maxHit: #move pawn with more hits to same colored pawns
                                    maxHit = crtHitSame
                                    self.board = copy.deepcopy(tempBoard)
                                if crtHitDiff < minHit: #move pawn with less hits to different colored pawns
                                    minHit = crtHitDiff
                                    self.board = copy.deepcopy(tempBoard)
            if minCost == currentCost: #stuck
                stop = True #stop searching