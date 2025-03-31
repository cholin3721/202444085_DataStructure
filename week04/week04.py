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
                return  # 내가 만들어 본거

    def __str__(self):
        # current = self.head
        # while current is not None :
        #     print(current.data, end=" -> ")
        #     current = current.link
        # return "END"
        # return "Linked List!"

        current = self.head
        out_texts = ""
        while current is not None :
            #out_texts = out_texts + str(current.data) + " -> "  # f스트링도 가능
            out_texts = out_texts + f"{current.data} -> "
            current = current.link
        return out_texts + "END"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)

ll.print()
print()
print(ll)