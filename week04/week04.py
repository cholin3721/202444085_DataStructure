import random


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


    def remove(self, target):
        current = self.head  # current 이동, 삭제할 노드의 링크도 완전하게 끊기 위해
        previous = None

        if current.data == target:  # 노드 자체랑 데이터랑 비교하는 것이 아닌, 노드의 데이터와 비교해야 함
            self.head = self.head.link
            current.link = None  # 삭제할 노드의 링크도 끊어주는 작업
            return

        while current :
            if current.data == target:
                previous.link = current.link  # 찾으면 지울 녀석 포인터를 전 노드 포인터에다 넣음
                current.link = None  # 삭제할 노드의 링크도 끊어주는 작업            previous = current
            current = current.link


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


    def search(self, target):
        current = self.head
        while current.link :
            if target == current.data:
                return f"{target} 을(를) 찾았습니다!"
            else:
                current = current.link  # move current
        return f"{target} 은(는) 링크드 리스트 안에 존재하지 않습니다!"

    def reverse(self):
        current = self.head
        previous = None
        while current :
            next = current.link  # 생각은 했는데 직접 시도 안해본 내 잘못.
            current.link = previous
            previous = current
            current = next
        self.head = previous

    def check_cycle(self):  # 생각해보니 인덱스를 지원하지 않아서 visited로 사이클을 체크하기엔 무리다.
        slow = self.head  # 이 알고리즘에 핵심은 사이클이 있다면 무한루프로 계속 돌아서 언젠간 따라잡는다는 이론. 아니면 일자로 쭉가서 false 반환
        fast = self.head
        while True :
            try :
                slow = slow.link
                fast = fast.link.link
                if slow is fast :
                    return True
            except :
                return False

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
# ll.remove(10)
# ll.remove(10)
# ll.remove(8)
ll.reverse()
print(ll)


# ll.print()
# print()
# print(ll)
# print()
# print(ll.search(10))  # __str__ method search method

# ll = LinkedList()
# for _ in range(20) :
#     # j = random.randint(1, 30)
#     # ll.append(j)
#     # print(j, end=" ")  책에 있는 코드,
#     ll.append(random.randint(1, 30))
# print(ll)
# print(ll.search(10))