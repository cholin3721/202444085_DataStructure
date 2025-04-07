# class Stack:
#     def __init__(self):
#         self.items = list()
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         return self.items[-1]
#
#
# s1 = Stack()
# s2 = Stack()
# print(s1.is_empty())
# s1.push("Data structure")
# print(s1.is_empty())
# print(s2.is_empty())
# s1.push("Database")
# print(s1.size())
# print(s1.peek())
# print(s1.size())
# print(s1.pop())
# print(s1.size())
# print(s1.peek())


# Stack with Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node  # top update

    def pop(self):
        if self.top is None:
            return "Stack is empty!"

        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None

        return popped_node.data


s1 = Stack()
print(s1.pop())
s1.push("Data structure")
s1.push("Database")
# print(s1.pop())
# print(s1.pop())
for i in range(3) :
    print(s1.pop())

s1 = list()
print(len(s1))
s1.append("Data structure") # push
s1.append("Database")  # push
print(len(s1))  # size
print(s1[-1])  # peek
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)