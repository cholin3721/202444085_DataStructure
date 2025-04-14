a_string = "Data Structure"
print(a_string[::-1])
print(reversed(a_string)) # 이건 reversed object와 주소가 나옴 약간
print("".join(reversed(a_string)))

def reversed_string(a_string):
    stack = []
    for i in a_string :
        stack.append(i)
    result = ""
    for _ in a_string :
        result += stack.pop()
    return result

print(reversed_string("Database"))