from abc import ABC, abstractmethod
from random import randint

def outRange(x, y) :
    return x < 0 or y < 0 or x > 7 or y > 7

def __eq__(self, other) :
    if isinstance(other, Pawn):
        return self.x == other.x and self.y == other.y

class Pawn(ABC):
    def __init__(self, isWhite):
        self.x = -1
        self.y = -1
        self.isWhite = isWhite

    def checkHit(self, listPawn, xAlpha, yAlpha):
        x = self.x + xAlpha
        y = self.y + yAlpha
        while not outRange(x,y):
            for pawn in listPawn:
                if pawn.x == x and pawn.y == y :
                    if pawn.isWhite == self.isWhite :
                        return (1, 0)
                    else :
                        return (0, 1)
            x += xAlpha
            y += yAlpha
        return (0, 0)

    @abstractmethod
    def hit(self, listPawn):
        pass

class Queen(Pawn):
    def hit(self, listPawn):
        same, diff = (0, 0)

        # cek utara
        temp1, temp2 = self.checkHit(listPawn, 0, -1)
        same += temp1
        diff += temp2
        # cek timur laut
        temp1, temp2 = self.checkHit(listPawn, 1, -1)
        same += temp1
        diff += temp2
        # cek timur
        temp1, temp2 = self.checkHit(listPawn, 1, 0)
        same += temp1
        diff += temp2
        # cek tenggara
        temp1, temp2 = self.checkHit(listPawn, 1, 1)
        same += temp1
        diff += temp2
        # cek selatan
        temp1, temp2 = self.checkHit(listPawn, 0, 1)
        same += temp1
        diff += temp2
        # cek barat daya
        temp1, temp2 = self.checkHit(listPawn, -1, 1)
        same += temp1
        diff += temp2
        # cek barat
        temp1, temp2 = self.checkHit(listPawn, -1, 0)
        same += temp1
        diff += temp2
        # cek barat laut
        temp1, temp2 = self.checkHit(listPawn, -1, -1)
        same += temp1
        diff += temp2

        return (same, diff)

class Knight(Pawn):
    def hit(self, listPawn):
        same, diff = (0, 0)
        for pawn in listPawn:
            if (abs(self.x - pawn.x) == 2 and abs(self.y - pawn.y) == 1) or (abs(self.x - pawn.x) == 1 and abs(self.y - pawn.y)) == 2:
                if self.isWhite == pawn.isWhite :
                    same += 1
                else :
                    diff += 1
        return (same, diff)
     

class Bishop(Pawn):
    def hit(self, listPawn):
        same, diff = (0, 0)

        # cek timur laut
        temp1, temp2 = self.checkHit(listPawn, 1, -1)
        same += temp1
        diff += temp2
        # cek tenggara
        temp1, temp2 = self.checkHit(listPawn, 1, 1)
        same += temp1
        diff += temp2
        # cek barat daya
        temp1, temp2 = self.checkHit(listPawn, -1, 1)
        same += temp1
        diff += temp2
        # cek barat laut
        temp1, temp2 = self.checkHit(listPawn, -1, -1)
        same += temp1
        diff += temp2

        return (same, diff)

class Rook(Pawn):
    def hit(self, listPawn):
        same, diff = (0,0)
        a = self.x - 1
        Found = False
        while ((a >= 0) and not Found):
            for pawn in listPawn:
                if pawn.y == self.y and pawn.x == a:
                    Found = True
                    if self.isWhite == pawn.isWhite :
                        same += 1
                    else :
                        diff += 1
            a -= 1
        a = self.x + 1
        Found = False
        while ((a <= 7) and not Found):
            for pawn in listPawn:
                if pawn.y == self.y and pawn.x == a:
                    Found = True
                    if self.isWhite == pawn.isWhite :
                        same += 1
                    else :
                        diff += 1
            a += 1
        a = self.y - 1
        Found = False
        while ((a >= 0) and not Found):
            for pawn in listPawn:
                if pawn.x == self.x and pawn.y == a:
                    Found = True
                    if self.isWhite == pawn.isWhite :
                        same += 1
                    else :
                        diff += 1
            a -= 1
        a = self.y + 1
        Found = False
        while ((a <= 7) and not Found):
            for pawn in listPawn:
                if pawn.x == self.x and pawn.y == a:
                    Found = True
                    if self.isWhite == pawn.isWhite :
                        same += 1
                    else :
                        diff += 1
            a += 1
        return (same, diff)

class Board:
    def __init__(self, listPawn):
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
        same, diff = (0, 0)
        for pawn in self.listPawn :
            temp1, temp2 = pawn.hit(self.listPawn)
            same += temp1
            diff += temp2

        return same

    def output(self):
        for x in range(0, 8):
            for y in range(0, 8):
                found = False
                for pawn in self.listPawn:
                    if pawn.x == x and pawn.y == y:
                        if isinstance(pawn, Queen):
                            print('Q', end='')
                            found = True
                            break
                        elif isinstance(pawn, Bishop):
                            print('B', end='')
                            found = True
                            break
                        elif isinstance(pawn, Rook):
                            print('R', end='')
                            found = True
                            break
                        elif isinstance(pawn, Knight):
                            print('K', end='')
                            found = True
                            break
                if not found:
                    print('.', end='')
            print('\n', end='')
            
        print(self.cost(), end=' ')
        print('0')

# for debug only
def printListPawn(listPawn) :
    for pawn in listPawn:
        if isinstance(pawn, Queen):
            print('Q', end=' ')
        elif isinstance(pawn, Bishop):
            print('B', end=' ')
        elif isinstance(pawn, Rook):
            print('R', end=' ')
        elif isinstance(pawn, Knight):
            print('K', end=' ')
        print(pawn.x, end=' ')
        print(pawn.y, end='\n')