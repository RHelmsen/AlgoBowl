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
    
    return board

def solve(i, board):
    fileName = './all_outputs/outputs/output_group'+str(i)+'.txt'
    outFile = open(fileName, 'w')
    trees = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='T':
                trees.append((i,j))

setup(974)

def main():
    inputNum=963
    while inputNum<=1024:
        board=setup(inputNum)
        solve(inputNum,board)
        inputNum+=1

