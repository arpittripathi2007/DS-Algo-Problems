def repeatedNumber(A):
    xor_A = A[0]
    x, y = 0, 0
    for item in A[1:]:
        xor_A = xor_A ^ item

    for i in range(1, len(A)+1):
        xor_A = xor_A ^ i

    right_most_bit = xor_A & ~(xor_A -1)

    for item in A:
        if(item & right_most_bit) != 0:
            x = x ^ item
        else:
            y = y ^ item
    
    for i in range(1, len(A)+1):
        if(i & right_most_bit) != 0:
            x = x ^ i
        else:
            y = y ^ i 
    return [x , y]
    
if __name__ == "__main__":
    print(repeatedNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))