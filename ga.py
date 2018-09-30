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

        # debug
        # for i in self.population:
        #     b.printListPawn(i.listPawn)
        #     print('---------------------')

        while True:

            tempPopulation = []
            
            # proses selection
            # sorting sesuai hasil FitnessFunction
            while len(self.population) > 0 and len(self.fitness) > 0:
                maks = max(self.fitness)
                print('maks self fitness = ',maks)
                idxToRemove = self.fitness.index(maks)
                tempPopulation.append(self.population[idxToRemove])
                del(self.population[idxToRemove])
                del(self.fitness[idxToRemove])                

            # individu terbaik dipertahankan
            self.population.append(tempPopulation[0])                    

            # proses crossover
            # individu dengan FitnessFunction terbaik menjadi parent utama
            # individu dengan FitnessFunction terendah dibuang
            for i in range (1, popNum-1):   
                if (i == 1):
                    self.population.append(self.crossOver(tempPopulation[0], tempPopulation[1]))                                       
                    self.population.append(self.crossOver(tempPopulation[1], tempPopulation[0]))   
                else:
                    self.population.append(tempPopulation[i])                   

            iteration += 1    

            # self.fitness diupdate setelah crossover
            for i in self.population:
               self.fitness.append(self.FitnessFunction(i))

            print("Iterasi ke", iteration, "; Max Fitness =", max(self.fitness), 'idx = ', self.fitness.index(max(self.fitness)))

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
            
            # proses mutasi
            p = uniform(0, 1)
            if (p >= 0.1):
                self.mutate(self.population)

                # self.fitness diupdate jika terjadi mutasi
                self.fitness = []
                for i in self.population:
                    self.fitness.append(self.FitnessFunction(i))
            
            # debug
            # idx=0
            # for i in self.population:
            #    b.printListPawn(i.listPawn)
            #    print('fitness func = ',self.FitnessFunction(i))
            #    print(self.fitness[idx])
            #    idx+=1
            #    print('---')
    
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

        # loop untuk memastikan posisi pawn beda-beda
        while True:
            
            # menentukan posisi pemotongan
            if (len(parent1.listPawn) != 0):
                cut = randint(2, len(parent1.listPawn) - 1)

            newListPawn = []

            i = 1
            for pawn1 in parent1.listPawn:
                newListPawn.append(copy.deepcopy(pawn1))
                if i == cut:
                    break
                i += 1

            j = 1
            for pawn2 in parent2.listPawn:
                if j >= (i + 1):
                    newListPawn.append(copy.deepcopy(pawn2))
                j += 1

            listPos = []

            for pawn in newListPawn:
                x = pawn.x
                y = pawn.y
                listPos.append((x, y))
            listPosSet = set(listPos)

            if len(listPos) == len(listPosSet):
                break

        individu = b.Board(newListPawn)

        return individu
    
    def mutate(self, parents):
        # parents adalah population
        # generate random index untuk memilih index board
        randIdx = randint(1, len(self.population)-1)
        selectedGene = parents[randIdx].listPawn

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
                print("x,y = ",x,y)
                selectedGene[randPawn].x = x
                selectedGene[randPawn].y = y
                break

        parents[randIdx].listPawn = copy.deepcopy(selectedGene)