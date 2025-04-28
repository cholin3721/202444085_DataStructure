class Node :
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None

    def append(self, data):
        node = Node(data)
        node.link = self.top
        self.top = node

    def pop(self):
        if self.top is None :
            print("there is no things to pop")
            return

        pop_things = self.top
        self.top = pop_things.link
        pop_things.link = None

        return pop_things.data

def check_bracket(expression) :
    stack = []
    brackets = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
    }

    for i in expression :
        if i in brackets :
            stack.append(brackets[i])
        elif i in brackets.values() :
            if not stack and i != stack.pop() :
                return False

    return True if not stack else False