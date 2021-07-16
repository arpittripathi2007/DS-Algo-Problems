def searchMatrix(matrix, target) -> bool:
    if(len(matrix) == 0):
        return False
    
    
    m = len(matrix)
    n = len(matrix[0])
    
    low = 0
    high = (m * n) -1
    
    while(low<=high):
        mid = (low + (high - low) // 2)
        
        if(matrix[mid//m][mid % m] == target):
            return True
        
        elif(matrix[mid//m][mid % m] < target):
            low = mid + 1
        else:
            high = mid - 1
            
    return False
    
if __name__ == "__main__":
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))