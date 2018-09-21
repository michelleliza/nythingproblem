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

a = np.zeros(shape=(8,8))
print(a)
fn = input("Please enter filename: ")
listPawn = readFile(fn)
print(listPawn)