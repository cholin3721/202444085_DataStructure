class Node :
    def __init__ (self, data, link=None) :
        self.data = data
        self.link = link


class Queue :
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size += 1
        node = Node(data)
        if self.front is None :
            self.front = node
            self.rear = node
        else :
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.front is None :
            raise IndexError("Queue is empty")
        q.size -= 1
        temp = self.front
        self.front = self.front.link
        temp.link = None
        if self.front is None :
            self.rear = None

        return temp.data


q = Queue()
q.enqueue("Database")
q.enqueue("Data Structure")

print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front, q.rear)
