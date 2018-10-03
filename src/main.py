import board as b
import sa
import copy
import ga
import hillclimb as hc

def readFile(filename):
    listPawn = []
    count = 0
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

        for i in range(0,n):
            count += 1
            if count > 64 :
                return None
            listPawn.append(copy.deepcopy(pawn))

    return listPawn

if __name__ == "__main__":
    # input filename from user
    fn = input("Please enter filename: ")
    listPawn = readFile(fn)

    if listPawn != None :
        print("Choose Local Search Algorithm")
        print("1. Hill Climbing")
        print("2. Simulated Annealing")
        print("3. Genetic Algorithm")
        option = input('Enter the number : ')
        if option == '1' : # hill climbing
            alg = hc.HillClimbing(listPawn)
            alg.board.output()
        elif option == '2' : # simulated annealing
            alg = sa.SimulatedAnnealing(listPawn)
            alg.board.output()
        elif option == '3' : # genetic algorithm

            while True:
                popNum = int(input("Enter number of population: "))

                if popNum > 1:
                    break
                print('Population number must be greater than 1')
                
            while True:
                maxIter = int(input("Enter number of maximum iteration: "))

                if maxIter > 0:
                    break
                print('Maximum iteration at least 1')

            alg = ga.GeneticAlgorithm(listPawn, popNum, maxIter)
            alg.result.output()
            # for debug purpose
            # b.printListPawn(alg.result.listPawn)
        else :
            print('Wrong number')
    else :
        print("Too much pawns (max: 64)")