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

class Queen(Pawn):
    def hit(self, listPawn):
        count = 0

        # cek utara
        count += checkHit(self, listPawn, 0, -1)
        # cek timur laut
        count += checkHit(self, listPawn, 1, -1)
        # cek timur
        count += checkHit(self, listPawn, 1, 0)
        # cek tenggara
        count += checkHit(self, listPawn, 1, 1)
        # cek selatan
        count += checkHit(self, listPawn, 0, 1)
        # cek barat daya
        count += checkHit(self, listPawn, -1, 1)
        # cek barat
        count += checkHit(self, listPawn, -1, 0)
        # cek barat laut
        count += checkHit(self, listPawn, -1, -1)

        return count
    
    def checkHit(self, listPawn, xAlpha, yAlpha):
        x = self.x + xAlpha
        y = self.y + yAlpha
        while not outRange(x,y):
            for pawn in listPawn:
                if pawn.x == x and pawn.y == y :
                    return 1
            x += xAlpha
            y += yAlpha
        return 0


class Knight(Pawn):
    def hit(self, listPawn):
        count = 0

class Bishop(Pawn):
    def hit(self, listPawn):
        count = 0

        for x, y in range(0, 8):
            if (abs(y - self.y)/abs(x - self.x)) == 1:
                for pawn in listPawn:
                    if (x == pawn.x) and (y == pawn.y):
                        count += 1

class Rook(Pawn):
    def hit(self, listPawn):
        count = 0

class Board:
    def __init__(color, listBidak):