def validPosition(row, col, numRows, numCols):
    # Helper function that returns a boolean if the row, col is a valid position on the grid
    return ((row > 0) and (row < numRows + 1) and (col > 0) and (col < numCols + 1))

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

def openOutputFile(filename):
    # Function open output file opens filename and returns the number of violations, the number of tents, and the list of tent information
    with open(filename, 'r') as inFile: # Open the file
        # Read first two input lines
        numViolations = int(inFile.readline().strip())
        numTents = int(inFile.readline().strip())
        # Get tent info: location and direction
        tents = []
        for line in inFile:
            parts = line.strip().split(" ")
            tents.append((int(parts[0]), int(parts[1]), parts[2]))
    return numViolations, numTents, tents

def openInputFile(filename):
    # Function open input file opens filename and returns the board, the row numbers, column numbers, number of rows, and number of cols
    with open(filename, 'r') as inFile: # Open the file
        # Get rows, cols
        dims = inFile.readline().strip().split(" ")
        numRows = int(dims[0])
        numCols = int(dims[1])
        rowNums = [int(r) for r in inFile.readline().split(" ")]            
        colNums = [int(c) for c in inFile.readline().split(" ")] 
        # Get board info
        board = []
        for line in inFile:
            row = list(line.strip())
            board.append(row)
    return board, rowNums, colNums, numRows, numCols

def validNumTents(numTents, tents):
    # Function validNumTrees checks if numTrees is correct
    return numTents == len(tents)

def validTentInfo(tents, board, numRows, numCols):
    # Function valid tent info checks if tent locations are valid and that they point to a tree (if applicable)
    directionLookup = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    for tent in tents: # loop through all tents
        tentRow = int(tent[0])
        tentCol = int(tent[1])
        tentDir = tent[2]
        # Check if tent position is actually on the board
        if not validPosition(tentRow, tentCol, numRows, numCols): 
            return False 
        # Check if tent position is avaiable on the board, anything other than '.' is not available
        if board[tentRow - 1][tentCol - 1] != '.': 
            return False
        # Check if where tent points to is actually on the board
        if tentDir in directionLookup: # Ensures we ingore any 'X'
            vert, horz = directionLookup[tentDir]
            if not validPosition(tentRow + vert, tentCol + horz, numRows, numCols): 
                return False
        # Check if where tent points to is a tree, anything other than 'T' is not a tree
        if board[tentRow - 1 + vert][tentCol - 1 + horz] != 'T': 
            return False
    return True # returns true if all tent info is valid

def placeTents(board, tents):
    for tent in tents:
        tentRow = int(tent[0])
        tentCol = int(tent[1])
        board[tentRow - 1][tentCol - 1] = "X"
    return board

def validViolations(numViolations, board, tents, rowNums, colNums):
    # Function valid violations calculates violations on output file and compares them to what was listed
    solution = placeTents(board, tents)
    trees = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='T':
                trees.append((i,j))
    actualViolations = calcViolations(solution, trees, tents, rowNums, colNums)
    return numViolations == actualViolations

def validOutput(inputFileName, outputFileName):
    # Function valid output inputs solution file and verifies its validity
    # A solution file is valid if:
        # Tents that say they point to trees actually point to them
        # Number of added tents is correct
        # Number of violations is correct
    board, rowNums, colNums, numRows, numCols = openInputFile(inputFileName)
    numViolations, numTents, tents = openOutputFile(outputFileName)
    if not validNumTents(numTents, tents): print("validNumTents failed")
    if not validTentInfo(tents, board, numRows, numCols): print("validTentInfo failed")
    if not validViolations(numViolations, board, tents, rowNums, colNums): print("validViolations failed")
    return validNumTents(numTents, tents) and validTentInfo(tents, board, numRows, numCols) and validViolations(numViolations, board, tents, rowNums, colNums)

def main():
    for num in range(1001,1002):
        inputFileName = './all_inputs/inputs/input_group'+str(num)+'.txt'
        outputFileName = './all_outputs/outputs/output_group'+str(num)+'.txt'
        if validOutput(inputFileName, outputFileName): 
            print("Valid Output File")
        else:
            print("Invalid Output File")

main()