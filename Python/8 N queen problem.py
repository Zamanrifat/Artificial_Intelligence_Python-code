''' Python3 program to solve N Queen Problem using 
backtracking '''
k = 1
 

def printSolution(board): 
 
    global k
    print(k, "-\n")
    k = k + 1
    for i in range(8): 
        for j in range(8):
            print(board[i][j], end = " ")
        print("\n")
    print("\n") 
 

def isSafe(board, row, col) :
     
    # Check this row on left side 
    for i in range(col): 
        if (board[row][i]): 
            return False
 
    # Check upper diagonal on left side 
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False;
        i -= 1
        j -= 1
 
    # Check lower diagonal on left side 
    i = row
    j = col
    while j >= 0 and i < 8:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True
 

def solveNQUtil(board, col) :
     
    
    if (col == 8): 
        printSolution(board) 
        return True
 
    
    res = False
    for i in range(8):
     
    
        if (isSafe(board, i, col)): 
         
            # Place of queen [i][col] 
            board[i][col] = 1; 
 
            # make true if possiable
            res = solveNQUtil(board, col + 1) or res; 
 
            
            board[i][col] = 0 # BACKTRACK 
         
    
    return res
 

def solveNQ() :
 
    board = [[0 for j in range(8)] 
                for i in range(8)]
 
    if (solveNQUtil(board, 0) == False): 
     
        print("There are no Solution") 
        return
    return
 

solveNQ() 