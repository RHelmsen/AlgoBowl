import io, sys, networkx as nx

def setup(inputNum):
    fileName = './all_inputs/inputs/input_group'+str(inputNum)+'.txt'
    inFile = open(fileName, 'r')

    board = []
    dims = inFile.readline().split(" ")
    rows = int(dims[0])     #number of rows
    cols = int(dims[1])     #number of cols
    rowNums = [int(r) for r in inFile.readline().split(" ")]            #number of tents for each row
    colNums = [int(c) for c in inFile.readline().split(" ")]            #number of tents for each col
    for i in range(rows):
        row = list(inFile.readline().strip())
        board.append(row)
    
    inFile.close()
    return board, rowNums, colNums

def solve(board, rowNums, colNums):
    trees = []
    tents = []
    solution = board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='T':
                trees.append((i,j))
    for tree in trees:
        tents.append((tree[0]-1,tree[1],'D'))
    return solution, tents   

def calcViolations(solution, tents, rowNums, colNums):
    violations=0
    return violations

def output(inputNum, v, tents):
    fileName = './all_outputs/outputs/output_group'+str(inputNum)+'.txt'
    outFile = open(fileName, 'w')
    outFile.write(str(v)+'\n')
    outFile.write(str(len(tents))+'\n')
    for tent in tents:
        outFile.write(str(tent[0]+1)+" "+str(tent[1]+1)+" "+tent[2]+'\n')
    
    outFile.close()

def main():
    inputNum=963
    while inputNum<=963:
        board, rowNums, colNums=setup(inputNum)
        solution, tents=solve(board, rowNums, colNums)
        violations=calcViolations(solution, tents, rowNums, colNums)
        output(inputNum, violations, tents)
        inputNum+=1

main()

