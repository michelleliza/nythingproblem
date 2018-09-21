import numpy as np
import board as b

def readFile(filename):
    listPawn = []
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        line2 = line.split(" ")
        if line2[1] == "KNIGHT":
            pawn = b.Knight()
        elif line2[1] == "BISHOP":
            pawn = b.Bishop()
        elif line2[1] == "ROOK":
            pawn = b.Rook()
        else:
            pawn = b.Queen()
        n = int(line2[2])
        for i in range(0,n):
            listPawn.append(pawn)
    return listPawn

def output(boardWhite, *args, **kwargs):
    if args :
        boardBlack = args[0]

    for x in range(0, 8):
        for y in range(0, 8):
            found = False
            for pawn in boardWhite.listPawn:
                if pawn.x == x and pawn.y == y:
                    if isinstance(pawn, b.Queen):
                        print('Q', end='')
                        found = True
                        break
                    elif isinstance(pawn, b.Bishop):
                        print('B', end='')
                        found = True
                        break
                    elif isinstance(pawn, b.Rook):
                        print('R', end='')
                        found = True
                        break
                    elif isinstance(pawn, b.Knight):
                        print('K', end='')
                        found = True
                        break

            for pawn in boardBlack.listPawn:
                if pawn.x == x and pawn.y == y:
                    if isinstance(pawn, b.Queen):
                        print('q', end='')
                        found = True
                        break
                    elif isinstance(pawn, b.Bishop):
                        print('b', end='')
                        found = True
                        break
                    elif isinstance(pawn, b.Rook):
                        print('r', end='')
                        found = True
                        break
                    elif isinstance(pawn, b.Knight):
                        print('k', end='')
                        found = True
                        break

            if not found:
                print('.', end='')
        print('\n', end='')
        
    print(boardWhite.cost() + boardBlack.cost(), end=' ')

    if not args:
        print('0', end='')

a = np.zeros(shape=(8,8))
print(a)
fn = input("Please enter filename: ")
listPawn = readFile(fn)
print(listPawn)