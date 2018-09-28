from random import randint, uniform
import board as b
import copy
import math

class GeneticAlgorithm():

    def __init__(self, listPawn, popNum, maxIteration):
        # initial config
        self.population = []
        self.fitness = []
        for i in range(popNum):
            bt = b.Board(listPawn)
            bt.initPawn()

            self.population.append(copy.deepcopy(bt))
            self.fitness.append(self.FitnessFunction(copy.deepcopy(bt)))

        iteration = 0
        maxFitness = self.maxAttack(self.population[0])

        #buat cek doang ini
        # for i in self.population:
        #     b.printListPawn(i.listPawn)
        #     print('---------------------')

        while True:

            tempPopulation = []

            # proses selection
            # sorting sesuai hasil FitnessFunction
            while len(self.population) > 0:
                maks = max(self.fitness)
                idxToRemove = self.fitness.index(maks)
                tempPopulation.append(self.population[idxToRemove])
                del(self.population[idxToRemove])
                del(self.fitness[idxToRemove])                

            # proses crossover
            # individu dengan FitnessFunction terbaik menjadi parent utama
            # individu dengan FitnessFunction terendah dibuang
            for i in range (1, popNum):
                if (i == 1):
                    self.population.append(self.crossOver(tempPopulation[0], tempPopulation[i]))                    
                    self.fitness.append(self.FitnessFunction(self.population[-1]))                    
                    self.population.append(self.crossOver(tempPopulation[i], tempPopulation[0]))
                    self.fitness.append(self.FitnessFunction(self.population[-1]))                    
                elif (i % 2 == 0):
                    self.population.append(self.crossOver(tempPopulation[0], tempPopulation[i]))
                    self.fitness.append(self.FitnessFunction(self.population[-1]))                    
                else:
                    self.population.append(self.crossOver(tempPopulation[i], tempPopulation[0]))
                    self.fitness.append(self.FitnessFunction(self.population[-1]))                    

            iteration += 1    

            #for i in self.population:
            #   b.printListPawn(i.listPawn)
            #    print('+++++++++')

            print("Iterasi ke", iteration, "; Max Fitness =", max(self.fitness))

            if iteration == maxIteration:
                print('Reach maximum steps')
                maks = max(self.fitness)
                idxResult = self.fitness.index(maks)
                self.result = self.population[idxResult]
                break

            if (maxFitness in self.fitness):
                idxResult = self.fitness.index(maxFitness)
                self.result = self.population[idxResult]
                break
            
            p = uniform(0, 1)
            if (p <= 0.2):
                self.mutate(self.population)
    
    # maksimum total attack tiap pawn
    def maxAttack(self, board):
        cnt_4 = 0
        cnt_8 = 0
        for pawn in board.listPawn:
            if isinstance(pawn, b.Bishop) or isinstance(pawn, b.Rook):
                cnt_4 += 1
            else:
                cnt_8 += 1
        return (cnt_4 * 4 + cnt_8 * 8)

    # total non-attacking pawn
    def FitnessFunction(self, board):
        return self.maxAttack(board) - board.cost()

    # setengah pawn baru dari parent1, setengah pawn dari parent2
    def crossOver(self, parent1, parent2):

        # menentukan posisi pemotongan
        cut = randint(2, len(parent1.listPawn) - 1)

        newListPawn = []

        i = 1
        for pawn1 in parent1.listPawn:
            newListPawn.append(pawn1)
            if i == len(parent1.listPawn) // cut:
                break
            i += 1

        j = 1
        for pawn2 in parent2.listPawn:
            if j >= (i + 1):
                newListPawn.append(pawn2)
            j += 1

        individu = b.Board(newListPawn)
        return individu
    
    def mutate(self, parents):
        # parents adalah population
        
        
        # generate random index untuk memilih index board
        randIdx = randint(0, len(self.population)-1)
        selectedGene = parents[randIdx].listPawn

        b.printListPawn(parents[randIdx].listPawn)
        print("------------------")
        # Select a random mutation point
        randPawn = randint(0, len(selectedGene)-1)
        
        # Select a random position for the pawn
        listPos = []
        for pawn in selectedGene:
            x = pawn.x
            y = pawn.y
            listPos.append((x, y))
        
        while True:
            x = randint(0,7)
            y = randint(0,7)
            if (x,y) not in listPos :
                selectedGene[randPawn].x = x
                selectedGene[randPawn].y = y
                break

        b.printListPawn(parents[randIdx].listPawn)
        print("------------------")
        return parents