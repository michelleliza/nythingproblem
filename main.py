import board as b
import sa
import copy
import ga

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

        if n != 0 :
            listPawn.append(pawn)
            for i in range(1,n):
                temp = copy.deepcopy(pawn)
                listPawn.append(temp)

    return listPawn

def output(board):
    for x in range(0, 8):
        for y in range(0, 8):
            found = False
            for pawn in board.listPawn:
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
            if not found:
                print('.', end='')
        print('\n', end='')
        
    print(board.cost(), end=' ')
    print('0')

fn = input("Please enter filename: ")
listPawn = readFile(fn)
popNum = int(input("Enter number of population: "))
maxIter = int(input("Enter number of maximum iteration: "))
tes = ga.GeneticAlgorithm(listPawn, popNum, maxIter)
output(tes.result)