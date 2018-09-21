from abc import ABC, abstractmethod

def inRange(x, y) :
    return x < 0 or y < 0 or x > 7 or y > 7

class Pawn(ABC):
    def __init__(self):
        self.x = -1
        self.y = -1

    @abstractmethod
    def hit(self, listPawn):
        pass

# ngaksesnya lansgung pawn.x atau pawn.y
class Queen(Pawn):
    def hit(self, listPawn):
        count = 0

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
    