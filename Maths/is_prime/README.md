## Factors of number

We can find the factors of all number with following approach


# CODE
================
```
def is_prime(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True
    
```
