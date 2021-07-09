def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    col_0 = 1
    
    for i in range(rows):
        if(matrix[i][0]) == 0:
            col_0 = 0
        for j in range(1, cols):
            if(matrix[i][j] == 0):
                matrix[i][0] = matrix[0][j] = 0
    
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if(matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0
        if col_0 == 0:
            matrix[i][0] = 0
    return matrix
    
if __name__ == "__main__":
    print(setZeroes([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]))