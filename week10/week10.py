class TreeNode :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def post_order(node) :
    if node is None :
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end= ' -> ')


def insert(root, value) :
    new_node = TreeNode()
    new_node.data = value

    if root is None :  # 첫 번째 노드 처리
        return new_node

    current = root
    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right

    return root


def search(root, search_value) :
    current = root

    while True:
        if search_value == current.data:
            return True

        elif search_value < current.data:
            if current.left is None :
                return False
            current = current.left

        else :
            if current.right is None :
                return False
            current = current.right

if __name__ == "__main__" :
    numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = None

    for number in numbers:
        root = insert(root, number)
    print("BST Structuring Complete")

    post_order(root)

    print()
    find_number = int(input("찾는 값 입력 : "))
    flag = search(root, find_number)  # 입력 부분을 search 함수에서 제거
    print(f"{find_number}을(를) 찾았습니다." if flag else f"{find_number}이(가) 존재하지 않습니다.")

    # while True:
    #     if find_number == current.data:
    #         print(f"{find_number}을(를) 찾았습니다.")
    #         break
    #
    #     elif find_number < current.data:
    #         if current.left is None :
    #             print(f"{find_number}을(를) 찾을 수 없습니다.")
    #             break
    #         current = current.left
    #
    #     else :
    #         if current.right is None :
    #             print(f"{find_number}을(를) 찾을 수 없습니다.")
    #             break
    #         current = current.right

