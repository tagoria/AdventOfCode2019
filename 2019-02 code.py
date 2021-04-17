import string
import fileinput
import os
import sys
import operator
import copy

def part1() :

    currentFile = __file__
    spacePosition = currentFile.find(" ")
    inputPath = currentFile[0:spacePosition] + " input.txt" 

    with open(inputPath, "r") as puzzleInput:
        intCodes = puzzleInput.read().split(",")

    intCodes = list(map(int,intCodes))
    intCodes[1] = 12
    intCodes[2] = 2
    operationPosition = 0
    operations = {1:operator.iadd,
    2:operator.mul}
    while (operationCode := intCodes[operationPosition]) in operations.keys() :
        pos1 = intCodes[operationPosition + 1]
        pos2 = intCodes[operationPosition + 2]
        pos3 = intCodes[operationPosition + 3]
        intCodes[pos3] = operations[operationCode](intCodes[pos1],intCodes[pos2])    
        operationPosition += 4

    print (intCodes[0])





def part2() :

    currentFile = __file__
    spacePosition = currentFile.find(" ")
    inputPath = currentFile[0:spacePosition] + " input.txt" 

    with open(inputPath, "r") as puzzleInput:
        initialMemory = puzzleInput.read().split(",")

    initialMemory = list(map(int,initialMemory))
    solved = False
    nounSolution = 0
    verbSolution = 0
    for i in range(0,100):
        for j in range(0,100):
            memory = copy.copy(initialMemory)
            memory[1] = i
            memory[2] = j
            operationPosition = 0
            operations = {1:operator.iadd,
            2:operator.mul}
            while (operationCode := memory[operationPosition]) in operations.keys() :
                pos1 = memory[operationPosition + 1]
                pos2 = memory[operationPosition + 2]
                pos3 = memory[operationPosition + 3]
                memory[pos3] = operations[operationCode](memory[pos1],memory[pos2])    
                operationPosition += 4
            if (memory[0] == 19690720):
                solved = True
                nounSolution = i
                verbSolution = j
                break
        if solved:
            break

    print (nounSolution * 100 + verbSolution)

part2()