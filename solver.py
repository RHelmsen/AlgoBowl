import io, sys, networkx as nx

def setup(inputNum):
    #fileName = './all_inputs/inputs/input_group'+str(inputNum)+'.txt'
    fileName='test_input.txt'
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
        directions = [(-1,0,'D'),(0,-1,'R'),(1,0,'U'),(0,1,'L')]
        temptents = []
        tentscores = []

        if(tree[0]==0):
            directions.remove((-1,0,'D'))       #can't go above a tree in the top row
        if(tree[1]==0):
            directions.remove((0,-1,'R'))       #can't go left of a tree in the leftmost col
        if(tree[0]==len(board)-1):
            directions.remove((1,0,'U'))        #can't go below a tree in the bottom row
        if(tree[1]==len(board[i])-1):
            directions.remove((0,1,'L'))        #can't go right of a tree in the rightmost col
        
        for dir in directions:
            tentloc = (tree[0]+dir[0],tree[1]+dir[1],dir[2])
            if solution[tentloc[0]][tentloc[1]]==".":
                temptents.append(tentloc)
                tentscores.append(rowNums[tentloc[0]]+colNums[tentloc[1]])
        
        optimal = tentscores.index(max(tentscores))
        tent=temptents[optimal]
        tents.append(tent)
        solution[tent[0]][tent[1]]="X"
        rowNums[tent[0]]-=1
        colNums[tent[1]]-=1

    return solution, tents   

def calcViolations(solution, tents, rowNums, colNums):
    violations=0
    return violations

def output(inputNum, v, tents):
    #fileName = './all_outputs/outputs/output_group'+str(inputNum)+'.txt'
    fileName='test_output.txt'
    outFile = open(fileName, 'w')
    outFile.write(str(v)+'\n')
    outFile.write(str(len(tents))+'\n')
    for tent in tents:
        outFile.write(str(tent[0]+1)+" "+str(tent[1]+1)+" "+tent[2]+'\n')
    
    outFile.close()

def main():
    inputNum=974
    while inputNum<=974:
        board, rowNums, colNums=setup(inputNum)
        solution, tents=solve(board, rowNums, colNums)
        violations=calcViolations(solution, tents, rowNums, colNums)
        output(inputNum, violations, tents)
        inputNum+=1

main()

