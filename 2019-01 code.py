import string
import fileinput
import os
import sys

def part1() :
    currentFile = __file__
    spacePosition = currentFile.find(" ")
    inputPath = currentFile[0:spacePosition] + " input.txt" 
    fuelNeeded = 0
    with open(inputPath, "r") as puzzleInput:
        for line in puzzleInput:
            massNeeded = int(line)
            fuelNeeded = fuelNeeded + ((massNeeded//3) - 2)
    print(fuelNeeded)

def part2() :
    currentFile = __file__
    spacePosition = currentFile.find(" ")
    inputPath = currentFile[0:spacePosition] + " input.txt" 
    fuelNeeded = 0
    with open(inputPath, "r") as puzzleInput:
        for line in puzzleInput:
            massNeeded = int(line)
            while (massNeeded := massNeeded//3 - 2)>0: 
                fuelNeeded = fuelNeeded + massNeeded
    print(fuelNeeded)

print (sys.version)
part2()