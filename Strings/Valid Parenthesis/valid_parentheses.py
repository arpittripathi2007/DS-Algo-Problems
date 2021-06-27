def isValid(s: str) -> bool:
    array_open = []
    open_bracket = ['(', '{', '[']
    closed_bracket = [')', '}', ']']
    list_s_copy = list(s)
    for item in list(s):
        if item in closed_bracket and len(array_open)==0:
            return False
        elif item in closed_bracket:
            char = item
            current_char = array_open.pop()

            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
        else:
            array_open.append(item)
    if len(array_open)>0:
        return False
    else:
        return True
    
if __name__ == "__main__":
    print(isValid("()[]{}"))