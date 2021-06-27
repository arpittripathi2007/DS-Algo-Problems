def decode(encoded, first):
    res = list()
    res.append(first)
    prev = first
    for item in encoded:
        xored = prev^item
        res.append(prev^item)
        prev = prev^item
    return res
    
if __name__ == "__main__":
    print(decode([6,2,7,3], 4))