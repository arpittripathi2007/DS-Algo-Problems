from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
    return matrix
    
if __name__ == "__main__":
    print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))