## Prime Numbers until N

Prime numbers until N using for Sieve of Eratosthenes:


# CODE
================
```
def sieve(n):
    if n < 2:
        return []
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if is_prime[i]:
            for j in range(i * 2, n+1, i):
                is_prime[j] = False
    return[i for i, b in enumerate(is_prime) if b]
    
```
