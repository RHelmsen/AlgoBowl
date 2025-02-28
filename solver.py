
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
        
        if len(temptents)>0:
            optimal = tentscores.index(max(tentscores))
            tent=temptents[optimal]
            tents.append(tent)
            solution[tent[0]][tent[1]]="X"
            rowNums[tent[0]]-=1
            colNums[tent[1]]-=1
    
    for row in range(len(solution)):
        if rowNums[row]>0:
            for col in range(len(solution[i])):
                if colNums[col]>0:
                    adj=[]
                    if row!=0:
                        adj.append(solution[row-1][col])
                        if col!=0:
                            adj.append(solution[row-1][col-1])
                        if col!=len(colNums)-1:
                            adj.append(solution[row-1][col+1])
                    if row!=len(rowNums)-1:
                        adj.append(solution[row+1][col])
                        if col!=0:
                            adj.append(solution[row+1][col-1])
                        if col!=len(colNums)-1:
                            adj.append(solution[row+1][col+1])
                    
                    if col!=0:
                        adj.append(solution[row][col-1])
                    
                    if col!=len(colNums)-1:
                        adj.append(solution[row][col+1])
                    
                    if solution[row][col]=='.' and "X" not in adj:
                        tents.append((row,col,'X'))
                        rowNums[row]-=1
                        colNums[col]-=1
                        solution[row][col]='X'
                if rowNums[row]==0:
                    break

    return solution, trees, tents, rowNums, colNums

def calcViolations(solution, trees, tents, rowNums, colNums):
    violations=0
    violations += sum(abs(row) for row in rowNums)+sum(abs(col) for col in colNums)
    
    for tent in tents:
        if tent[2]=='U':
            if (tent[0]-1,tent[1]) not in trees:
                violations+=1
            else:
                trees.remove((tent[0]-1,tent[1]))
        if tent[2]=='D':
            if solution[tent[0]+1][tent[1]]!='T':
                violations+=1
            else:
                trees.remove((tent[0]+1,tent[1]))
        if tent[2]=='L':
            if solution[tent[0]][tent[1]-1]!='T':
                violations+=1
            else:
                trees.remove((tent[0],tent[1]-1))
        if tent[2]=='R':
            if solution[tent[0]][tent[1]+1]!='T':
                violations+=1
            else:
                trees.remove((tent[0],tent[1]+1))
        if tent[2]=='X':
            violations+=1

        directions = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)] 

        if(tent[0]==0):
            if(tent[1]==0):
                directions.remove((0,-1))
                directions.remove((1,-1))
            if(tent[1]==len(solution[0])):
                directions.remove((0,1))
                directions.remove((1,1))
            directions.remove((-1,0))       #can't go above a tree in the top row
            directions.remove((-1,1))
            directions.remove((-1,-1))
        elif(tent[1]==0):
            if(tent[0]==0):
                directions.remove((-1,0))
                directions.remove((-1,1))
            if(tent[0]==len(solution)):
                directions.remove((1,0))
                directions.remove((1,1))
            directions.remove((0,-1))       #can't go left of a tree in the leftmost col
            directions.remove((1,-1))
            directions.remove((-1,-1))
        elif(tent[0]==len(solution)-1):
            if(tent[1]==0):
                directions.remove((0,-1))
                directions.remove((-1,-1))
            if(tent[1]==len(solution[0])):
                directions.remove((0,1))
                directions.remove((-1,1))
            directions.remove((1,0))        #can't go below a tree in the bottom row
            directions.remove((1,1))
            directions.remove((1,-1))
        elif(tent[1]==len(solution[0])-1):
            if(tent[0]==0):
                directions.remove((-1,0))
                directions.remove((-1,-1))
            if(tent[0]==len(solution)):
                directions.remove((1,0))
                directions.remove((1,-1))
            directions.remove((0,1))        #can't go right of a tree in the rightmost col
            directions.remove((1,1))
            directions.remove((-1,1))
        adjacency = False
        for dir in directions:
            tentadj = (tent[0]+dir[0],tent[1]+dir[1])
            for tent2 in tents:
                if(tentadj[0]==tent2[0]) and tentadj[1]==tent2[1]:
                    adjacency=True
                    break
            if adjacency:
                violations+=1
                break

    violations+=len(trees)


    


    return violations

def output(inputNum, v, tents):
    fileName = './all_outputs/outputs/output_group'+str(inputNum)+'.txt'
    fileName2 = './all_outputs/outputs2/output_group'+str(inputNum)+'-2.txt'
    outFile = open(fileName2, 'w')
    inFile = open(fileName, 'r')
    outFile.write(str(v)+'\n')
    outFile.write(str(len(tents))+'\n')
    for tent in tents:
        outFile.write(str(tent[0]+1)+" "+str(tent[1]+1)+" "+tent[2]+'\n')
    print(inputNum,int(inFile.readline().strip())-v)
    outFile.close()

def main():
    inputNum=969
    while inputNum<=1024:
        if inputNum==1020:
            continue
        board, rowNums, colNums=setup(inputNum)
        solution, trees, tents, rowNums, colNums=solve(board, rowNums, colNums)
        violations=calcViolations(solution, trees, tents, rowNums, colNums)
        output(inputNum, violations, tents)
        inputNum+=1

main()

