class Node :
    def __init__(self, data = None, link = None ):
        self.data = data
        self.link = None


class Queue :
    def __init__(self):
        self.rear = None
        self.front = None
        self._size = 0


    def enqueue(self, data):
        node = Node(data)
        if self.rear is None :
            self.front = node
            self.rear = node

        else :
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.front is None :
            print("there is no things to dequeue")
            return

        temp = self.front
        self.front = self.front.link
        temp.link = None

        if self.front is None :  # queue 가 비었을때
            self.rear = None

        return temp.data