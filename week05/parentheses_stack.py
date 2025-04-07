def is_valid_brackets(expression : str) -> bool :  # parameter data type, type hint
    stack = []
    parentheses = {
        "(" : lambda:stack.append("("),
        ")": lambda:stack.pop(),
        "{": lambda: stack.append("{"),
        "}": lambda: stack.pop()
    }

    for c in expression :
        if c in parentheses :
            try:
                check = parentheses[c]()
                if c == "}" and check != "{":
                    return False
                if c == ")" and check != "(":
                    return False
            except IndexError:
                print("index error")
                return False

    return not stack

def is_valid_brackets_ver2(expression : str) -> bool :
    stack = []
    brackets = {
        "}" : "{",
        "]" : "[",
        ")" : "(",
    }
    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys() :
            if not stack or stack.pop() != brackets[letter] :
                return False
    return not stack

print(is_valid_brackets_ver2("{(2+3})"))