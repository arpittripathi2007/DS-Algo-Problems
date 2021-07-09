def multiple(A):
    set_visit = [1]
    visited_rem = set([])

    while(len(set_visit)>0):
        check_elem = set_visit.pop(0) #popping latest element to check
        rem = check_elem % A
        if(rem == 0):
            return check_elem
        else:
            if (rem not in visited_rem):
                visited_rem.add(rem)
                set_visit.append(int(str(check_elem)+'0'))
                set_visit.append(int(str(check_elem)+'1'))

if __name__ == "__main__":
    print(multiple(55))