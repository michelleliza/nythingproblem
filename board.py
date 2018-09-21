from abc import ABC, abstractmethod
from random import randint

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
        count += self.checkHit(listPawn, 0, -1)
        # cek timur laut
        count += self.checkHit(listPawn, 1, -1)
        # cek timur
        count += self.checkHit(listPawn, 1, 0)
        # cek tenggara
        count += self.checkHit(listPawn, 1, 1)
        # cek selatan
        count += self.checkHit(listPawn, 0, 1)
        # cek barat daya
        count += self.checkHit(listPawn, -1, 1)
        # cek barat
        count += self.checkHit(listPawn, -1, 0)
        # cek barat laut
        count += self.checkHit(listPawn, -1, -1)

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

        for x, y in range(0, 8):
            if (abs(y - self.y)/abs(x - self.x)) == 1:
                for pawn in listPawn:
                    if (x == pawn.x) and (y == pawn.y):
                        count += 1
        
        return count

class Rook(Pawn):
    def hit(self, listPawn):
        count = 0
        a = self.x - 1
        Found = False
        while ((a >= 0) and not Found):
            for pawn in listPawn:
                if pawn.y == self.y and pawn.x == a:
                    Found = True
                    count += 1
            a -= 1
        a = self.x + 1
        Found = False
        while ((a <= 7) and not Found):
            for pawn in listPawn:
                if pawn.y == self.y and pawn.x == a:
                    Found = True
                    count += 1
            a += 1
        a = self.y - 1
        Found = False
        while ((a >= 0) and not Found):
            for pawn in listPawn:
                if pawn.x == self.x and pawn.y == a:
                    Found = True
                    count += 1
            a -= 1
        a = self.y + 1
        Found = False
        while ((a <= 7) and not Found):
            for pawn in listPawn:
                if pawn.x == self.x and pawn.y == a:
                    Found = True
                    count += 1
            a += 1
        return count

class Board:
    def __init__(self, color, listPawn):
        self.color = color
        self.listPawn = listPawn
        self.initPawn()

    def initPawn(self):
        listPos = []
        for pawn in self.listPawn:
            while True:
                x = randint(0,7)
                y = randint(0,7)
                if (x,y) not in listPos :
                    listPos.append((x, y))
                    pawn.x = x
                    pawn.y = y
                    break

    def cost(self):
        count = 0
        for pawn in self.listPawn :
            count += pawn.hit(self.listPawn)

        return count