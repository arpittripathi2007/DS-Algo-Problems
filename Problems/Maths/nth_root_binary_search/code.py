import math


def NthRoot(n, m):
    # Code here
    start = 0
    end = 9
    eps = 1e-9

    mid = (start + end)/2


    while(mid ** n != float(m)):
        if(mid**n > m):
            end = mid-1
        else:
            start = mid+1
        mid = (start+end)/2

    return round(mid)


if __name__ == '__main__':
    is_prime = NthRoot(2, 9)
    print(is_prime)
