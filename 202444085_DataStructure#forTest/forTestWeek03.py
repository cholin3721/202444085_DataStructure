class Node :
    def __init__(self, data):
        self.data = data
        self.link = None


class Linked_list :
    def __init__(self):
        self.head = None


    def append(self, data):
        node = Node(data)
        if self.head is None :
            self.head = node
            return

        current = self.head
        while current.link :
            current = current.link
        current.link= node

    def search(self, target):
        if self.head is None :
            print("There is no such Things in the lInked list")
            return False

        current = self.head
        while current :
            if current.data == target:
                return True
            current = current.link
        return False


    def remove(self, target):
        if self.head is None :
            print("there is no elements to remove")
            return
        current = self.head
        previous = None

        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return

        while current :
            if current.data == target:
                previous.link = current.link
                current.link = None
                return
            previous = current
            current = current.link



    def __str__ (self) :
        if self.head is None :
            return "This Linked List is Empty"
        out_text = ""
        current = self.head
        while current:
            out_text += f"{current.data} -> "
            current = current.link
        out_text += "End"
        return out_text

ll = Linked_list()
ll.append("1")
ll.append(2)
ll.append("3")
ll.append("Seoul")

print(ll)