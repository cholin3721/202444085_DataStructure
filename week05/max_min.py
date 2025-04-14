class minStack :
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, num):
        if len(self.main) == 0 :
            self.min.append(num)
        elif num <= self.min[-1] :
            self.min.append(num)
        else :
            self.min.append(self.min[-1])
        self.main.append(num)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]