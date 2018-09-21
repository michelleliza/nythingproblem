from abc import ABC, abstractmethod

def outRange(x, y) :
    return x < 0 or y < 0 or x > 7 or y > 7

def __eq__(self, other) :
    if isinstance(other, Pawn):
        return self.x == other.x and self.y == other.y

class Pawn(ABC):
    def __init__(self):
        self.x = -1
        self.y = -1

    @abstractmethod
    def hit(self, listPawn):
        pass

# ngaksesnya langsung pawn.x atau pawn.y
class Queen(Pawn):
    def hit(self, listPawn):
        count = 0

        # cek atas
    
    def checkHit(self, listPawn, xAlpha, yAlpha):
        x = self.x
        y = self.y
        while inRange(x,y):



class Knight(Pawn):
    def hit(self, listPawn):
        count = 0

class Bishop(Pawn):
    def hit(self, listPawn):
        count = 0

class Rook(Pawn):
    def hit(self, listPawn):
        count = 0

class Board:
    def __init__(color, listBidak):
    