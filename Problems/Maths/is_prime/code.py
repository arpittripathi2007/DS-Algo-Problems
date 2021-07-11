import math


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


if __name__ == '__main__':
    n = int(input('Enter Limit in Positive Integer: '))
    is_prime = is_prime(n)
    print(is_prime)
