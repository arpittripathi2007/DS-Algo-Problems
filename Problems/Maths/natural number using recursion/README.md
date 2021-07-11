## Printing the natural number using recursion in ascending as well as descending order

# CODE
================
```
def all_natural_desc(arr):
    if arr >= 1:
        print(arr)
        return all_natural_desc(arr-1)
    pass


def all_natural_asc(arr, i):
    if i <= arr:
        print(i)
        return all_natural_asc(arr, i+1)
    pass


if __name__ == '__main__':
    N = int(input('Enter Limit in Positive Integer: '))
    option = int(input('Choose Option \n 1 for ascending \n 2 for descending: '))
    print(option, N)
    if option == 2:
        all_natural_desc(N)
    elif option == 1:
        all_natural_asc(N, 0)
    
```
