## Most Optimised Solution n+m C m-1
def uniquePaths(m: int, n: int) -> int:
    N = n + m -2
    r = m - 1
    res = 1
    
    for i in range(1, r+1):
        res *= (N-r + i)/i
    return int(round(res))

## Recursion
def countPathRecursion(i, j, n, m):
    if(i==(n-1) and j==(m-1)):
        return 1
    if(i>=n or j>=m):
        return 0
    else:
        return countPathRecursion(i+1, j, n, m)+ countPathRecursion(i, j+1, n, m)

## DynamicProgramming: creating the hash table for visited co-ordinate(node)
def countPathDP(i, j, n, m, dp):
    if(i==(n-1) and j==(m-1)):
        return 1
    if(i>=n or j>=m):
        return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    else:
        dp[i][j] = (countPathDP(i+1, j, n, m, dp) + countPathDP(i, j+1, n, m, dp))
        return dp[i][j]

def uniquePathsRecursion(m, n):
    return countPathRecursion(0, 0, m, n)

def uniquePathsDP(m, n):
    dp = [ [ -1 for i in range(n) ] for j in range(m) ]
    return countPathDP(0, 0, m, n, dp)
    
if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths(m, n))
    print(uniquePathsRecursion(n, m))
    print(uniquePathsDP(n, m))