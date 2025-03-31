class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList :
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head :
            self.head = Node(data)
            return
        current = self.head
        while current.link :
            current = current.link
        current.link = Node(data)

    def print(self):
        if self.head == None :
            print("Nothing connected")
            return
        else :
            current = self.head
        while current.data != None :
            print(current.data)
            current = current.link
            if current == None :
                break

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)

ll.print()
print(ll)