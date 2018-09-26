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
            self.population.append(bt)
            self.fitness.append(self.FitnessFunction(bt))

        iteration = 0
        maxFitness = self.maxAttack(self.population)

        while True:

            tempPopulation = []
            while len(self.population) > 0:
                maks = max(self.fitness)
                idxToRemove = self.fitness.index(maks)
                tempPopulation.append(self.population[idxToRemove])
                del(self.population[idxToRemove])
                del(self.fitness[idxToRemove])                

            self.population = []
            self.fitness = []
            for i in range(0, 2, popNum):
                new1 = self.crossOver(tempPopulation[i], tempPopulation[i+1])
                new2 = self.crossOver(tempPopulation[i+1], tempPopulation[i])
                self.population.append(new1)
                self.population.append(new2)
                self.fitness.append(new1)
                self.fitness.append(new2)

            iteration += 1    
 
            if iteration == 1 or (maxFitness in self.fitness):
                break
            
            if (uniform(0, 1) >= 0.2):
                self.mutate(self.population)
        
    def maxAttack(self, board):
        cnt_4 = 0
        cnt_8 = 0
        for pawn in board.listPawn:
            if isinstance(pawn, b.Bishop) or isinstance(pawn, b.Rook):
                cnt_4 += 1
            else:
                cnt_8 += 1
        return (cnt_4 * 4 + cnt_8 * 8)

    def FitnessFunction(self, board):
        return self.maxAttack(board) - board.cost()

    #Setengah pawn dari parent1, setengah pawn dari parent2
    def crossOver(self, parent1, parent2):

        newListPawn = []

        i = 1
        for pawn1 in parent1.listPawn:
            newListPawn.append(pawn1)
            if i == len(parent1.listPawn) // 2:
                break
            i += 1

        i = 1
        for pawn2 in parent2.listPawn:
            if i == len(parent2.listPawn) // 2 + 1:
                newListPawn.append(pawn2)
            i += 1

        individu = b.Board(newListPawn)

        return individu
    
    def mutate(self, parents):
        return 0