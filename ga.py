from random import randint, uniform
import board as b
import copy
import math

class GeneticAlgorithm():

    def __init__(self, listPawn):
        # initial config
        self.board1 = b.Board(listPawn)
        self.board2 = b.Board(listPawn)
        self.board3 = b.Board(listPawn)
        self.board4 = b.Board(listPawn)
        self.population = [self.board1, self.board2, self.board3, self.board4]
        self.fitness = [self.FitnessFunction(self.population[0]), self.FitnessFunction(self.population[1]), self.FitnessFunction(self.population[2]), self.FitnessFunction(self.population[3])]
        
        iteration = 0
        maxFitness = self.maxAttack(self.board1)

        while True:

            if iteration == 1000 or (maxFitness in self.fitness):
                break

            tempPopulation = []
            
            for i in range(len(self.population)):
                p = self.population[self.fitness.index(max(self.fitness))]
                tempPopulation.append(p)
                self.fitness.remove(max(self.fitness))
                self.population.remove(p)
            
            self.population = [
                self.crossOver(tempPopulation[0], tempPopulation[1]),
                self.crossOver(tempPopulation[1], tempPopulation[0]),
                self.crossOver(tempPopulation[2], tempPopulation[3]),
                self.crossOver(tempPopulation[3], tempPopulation[2])
            ]
            self.fitness = [self.FitnessFunction(self.population[0]), self.FitnessFunction(self.population[1]), self.FitnessFunction(self.population[2]), self.FitnessFunction(self.population[3])]
            
        
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