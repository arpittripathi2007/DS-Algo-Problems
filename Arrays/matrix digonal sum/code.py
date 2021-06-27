def diagonalSum(self, mat: List[List[int]]) -> int:
    len_ = len(mat)
    sum_ = 0
    
    for i in range(len_):
        sum_ += mat[i][i]
    
    j = len_ - 1
    for i in range(len_):
        sum_ += mat[i][j]
        j -= 1
    if len_%2 != 0:
        sum_ -= mat[len_//2][len_//2]
    return sum_
    
if __name__ == "__main__":
    print(diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))