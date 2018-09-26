import board as b
import sa
import copy
import ga
import hillclimb as hc

def readFile(filename):
    listPawn = []
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        line2 = line.split(" ")
        if line2[1] == "KNIGHT":
            if line2[0].lower() == 'black' :
                pawn = b.Knight(False)
            else :
                pawn = b.Knight(True)
        elif line2[1] == "BISHOP":
            if line2[0].lower() == 'black' :
                pawn = b.Bishop(False)
            else :
                pawn = b.Bishop(True)
        elif line2[1] == "ROOK":
            if line2[0].lower() == 'black' :
                pawn = b.Rook(False)
            else :
                pawn = b.Rook(True)
        else:
            if line2[0].lower() == 'black' :
                pawn = b.Queen(False)
            else :
                pawn = b.Queen(True)
        n = int(line2[2])

        if n != 0 :
            listPawn.append(pawn)
            for i in range(1,n):
                temp = copy.deepcopy(pawn)
                listPawn.append(temp)

    return listPawn

fn = input("Please enter filename: ")
listPawn = readFile(fn)

print("Choose Local Search Algorithm")
print("1. Hill Climbing")
print("2. Simulated Annealing")
print("3. Genetic Algorithm")
option = input('Enter the number : ')
if option == '1' :
    alg = hc.HillClimbing(listPawn)
    alg.board.output()
elif option == '2' :
    alg = sa.SimulatedAnnealing(listPawn)
    alg.board.output()
else :
    popNum = int(input("Enter number of population: "))
    maxIter = int(input("Enter number of maximum iteration: "))
    alg = ga.GeneticAlgorithm(listPawn, popNum, maxIter)
    alg.result.output()
