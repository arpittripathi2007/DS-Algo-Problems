def myPow(x: float, n: int) -> float:
    num = n if n >= 0 else n*-1
    ans = 1
    while(num > 0):
        if(num % 2 == 1):
            ans = ans * x
            num = num - 1
        else:
            x = x * x
            num = num / 2
            
    ans  = ans if n >= 0 else 1/(ans)
    
    return ans
    
if __name__ == "__main__":
    print(myPow(2.00000, 10))