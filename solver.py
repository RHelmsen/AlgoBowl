import io, sys, networkx as nx

def setup(i):
    fileName = './all_inputs/inputs/input_group'+str(i)+'.txt'
    inFile = open(fileName, 'r')

    board = []
    dims = inFile.readline().split(" ")
    rows = int(dims[0])
    cols = int(dims[1])
    rowNums = [int(r) for r in inFile.readline().split(" ")]
    colNums = [int(c) for c in inFile.readline().split(" ")]
    for i in range(rows):
        row = list(inFile.readline().strip())
        board.append(row)
    
    return board, rowNums, colNums

def solve(board, rowNums, colNums):
    trees = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='T':
                trees.append((i,j))
    
    for tree in range(len(trees)):
        print()

def calcViolations(board, sol):
    violations=0

def output(i, v, t, sol):
    fileName = './all_outputs/outputs/output_group'+str(i)+'.txt'
    outFile = open(fileName, 'w')

def main():
    inputNum=963
    while inputNum<=1024:
        board, rowNums, colNums=setup(inputNum)
        solution, numTents=solve(board, rowNums, colNums)
        violations=calcViolations(numTents, solution, rowNums, colNums)
        output(inputNum, violations, numTents, solution)
        inputNum+=1

