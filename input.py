#input.py

from board.py import *

def readFile(filename):
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        line2 = line.split(" ")
        print(line2)

fn = input()
readFile(fn)