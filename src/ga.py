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

        # proses selection
        # sorting sesuai hasil FitnessFunction
        self.population = sorted(self.population, key=self.FitnessFunction, reverse=True)

        iteration = 0
        maxFitness = self.maxAttack(self.population[0])

        while True:
            # proses crossover
            # individu dengan FitnessFunction terbaik ke-1 dan 2 menjadi parent
            # individu dengan FitnessFunction terendah dibuang
            del(self.population[-2:])
            self.population.extend(self.crossOver(self.population[0], self.population[1]))

            # sorting sesuai hasil FitnessFunction
            self.population = sorted(self.population, key=self.FitnessFunction, reverse=True)

            # individu dengan FitnessFunction terbaik ke-2 dan 3 menjadi parent
            # individu dengan FitnessFunction terendah dibuang
            if len(self.population) > 4:
                del(self.population[-2:])
                self.population.extend(self.crossOver(self.population[1], self.population[2]))

                # sorting sesuai hasil FitnessFunction
                self.population = sorted(self.population, key=self.FitnessFunction, reverse=True)

            self.fitness = self.PopulationFitness(self.population)
            iteration += 1

            # print("Iterasi ke", iteration, "; Max Fitness =", max(self.fitness), self.fitness)

            if iteration == maxIteration:
                print('Reach maximum steps')
                # maks = max(self.fitness)
                # idxResult = self.fitness.index(maks)
                self.result = self.population[0]
                break

            if (maxFitness in self.fitness):
                print('Iterasi ke', iteration)
                # idxResult = self.fitness.index(maxFitness)
                self.result = self.population[0]
                break

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

    def PopulationFitness(self, population):
        fitness = []
        for p in range(len(self.population)):
            fitness.append(self.FitnessFunction(self.population[p]))
        return fitness

    # setengah pawn baru dari parent1, setengah pawn dari parent2
    def crossOver(self, parent1, parent2):

        # menentukan posisi pemotongan
        if (len(parent1.listPawn) != 0):
            cut = randint(1, len(parent1.listPawn) - 1)

        newListPawn1 = []
        newListPawn2 = []

        listPos1 = []
        listPos2 = []
        
        for i in range(0, cut):
            pawn1 = parent1.listPawn[i]
            pawn2 = parent2.listPawn[i]

            newListPawn1.insert(i, copy.deepcopy(pawn1))
            listPos1.append((pawn1.x, pawn1.y))
            # print(listPos1)

            newListPawn2.insert(i, copy.deepcopy(pawn2))
            listPos2.append((pawn2.x, pawn2.y))
            # print(listPos2)

        
        for j in range(cut, len(parent1.listPawn)):
            pawn1 = parent1.listPawn[j]
            pawn2 = parent2.listPawn[j]

            if (pawn2.x, pawn2.y) not in listPos1:
                newListPawn1.insert(j, copy.deepcopy(pawn2))
                listPos1.append((pawn2.x, pawn2.y))                
            else:
                newListPawn1.insert(j, copy.deepcopy(pawn1))
                listPos1.append((pawn1.x, pawn1.y))                                
            # print(listPos1)

            if (pawn1.x, pawn1.y) not in listPos2:
                newListPawn2.insert(j, copy.deepcopy(pawn1))
                listPos2.append((pawn1.x, pawn1.y))

            else:
                newListPawn2.insert(j, copy.deepcopy(pawn2))
                listPos2.append((pawn2.x, pawn2.y))
            # print(listPos2)

        individu1 = b.Board(newListPawn1)
        individu2 = b.Board(newListPawn2)

        return [self.mutate(individu1), self.mutate(individu2)]

    def mutate(self, parents):
        # parents adalah board

        # Select a random mutation point
        randPawn = randint(0, len(parents.listPawn)-1)

        # Select a random position for the pawn
        listPos = self.pawnPosition(parents.listPawn)

        while True:
            x = randint(0,7)
            y = randint(0,7)
            if (x,y) not in listPos :
                parents.listPawn[randPawn].x = x
                parents.listPawn[randPawn].y = y
                break
        return parents

    def pawnPosition(self, listPawn):
        listPos = []
        for pawn in listPawn:
            x = pawn.x
            y = pawn.y
            listPos.append((x, y))
        return listPos