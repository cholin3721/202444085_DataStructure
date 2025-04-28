class Min :
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def append(self, num):
        self.main_stack.append(num)
        if not self.min_stack :
            self.min_stack.append(num)

        elif self.min_stack[-1] >= num :
            self.min_stack.append(num)

        else :
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    def get_min(self):
        return self.min_stack[-1]


def reversed_string(expression) :
    temp = []
    for i in expression :
        temp.append(i)

    out_text = ""

    for _ in temp :
        out_text += temp.pop()

    return out_text


