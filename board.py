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
        for pawn in listPawn:
            if abs(self.x - pawn.x) == 2 and abs(self.y - pawn.y) == 1 or abs(self.x - pawn.x) == 1 and abs(self.y - pawn.y) == 2:
                count = count + 1
        return count
     

class Bishop(Pawn):
    def hit(self, listPawn):
        count = 0

class Rook(Pawn):
    def hit(self, listPawn):
        count = 0
        a = self.x - 1
        Found = False
        while ((a >= 0) and not Found):
            for pawn in listPawn:
                if pawn.y == self.y:
                    Found = True
                    count += 1
            a -= 1
        a = self.x + 1
        Found = False
        while ((a <= 7) and not Found):
            for pawn in listPawn:
                if pawn.y == self.y:
                    Found = True
                    count += 1
            a += 1
        a = self.y - 1
        Found = False
        while ((a >= 0) and not Found):
            for pawn in listPawn:
                if pawn.x == self.x:
                    Found = True
                    count += 1
            a -= 1
        a = self.y + 1
        Found = False
        while ((a <= 7) and not Found):
            for pawn in listPawn:
                if pawn.x == self.x:
                    Found = True
                    count += 1
            a += 1
        return count

class Board:
    def __init__(color, listBidak):