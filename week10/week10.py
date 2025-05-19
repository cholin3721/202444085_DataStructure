from numpy.ma.core import left_shift


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


def insert(node, value) :
    new_node = TreeNode()
    new_node.data = value

    if node is None :  # 첫 번째 노드 처리
        return new_node

    current = node
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

    return node


def search(node, search_value) :
    current = node

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

def delete_right(node, value) :
    if node is None :
        return None
    if value < node.data :
        node.left = delete_right(node.left, value)
    elif value > node.data :
        node.right = delete_right(node.right, value)
    else :  # 삭제할 노드 발견
        # 자식 노드가 1개 이거나 leaf 노드일 경우
        if node.left is None :
            return node.right
        elif node.right is None :
            return node.left
        else :
            min_larger_node = node.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left  # move
            # 이 두 코드는 무조건 실행되어야 하는 코드. 즉, 이게 while문 안에 있으면 결국 찾았을때
            node.data = min_larger_node.data
            # 찾은 노드 제외하고 오른쪽에서 삭제
            node.right = delete_right(node.right, min_larger_node.data)

    return node


def delete_left(node, value) :
    if node is None :
        return None
    if value < node.data :
        node.left = delete_left(node.left, value)
    elif value > node.data :
        node.right = delete_left(node.right, value)
    else :  # 삭제할 노드 발견
        # 자식 노드가 1개 이거나 leaf 노드일 경우
        if node.left is None :
            return node.right
        elif node.right is None :
            return node.left
        else :
            max_smaller_node = node.left
            while max_smaller_node.right:
                max_smaller_node = max_smaller_node.right  # move
            # 이 두 코드는 무조건 실행되어야 하는 코드. 즉, 이게 while문 안에 있으면 결국 찾았을때
            node.data = max_smaller_node.data
            # 찾은 노드 제외하고 오른쪽에서 삭제
            node.left = delete_left(node.left, max_smaller_node.data)
    return node

if __name__ == "__main__" :
    numbers = [10, 15, 8, 3, 9, 14]
    root = None

    for number in numbers:
        root = insert(root, number)
    print("BST Structuring Complete")

    post_order(root)

    print()
    find_number = int(input("찾는 값 입력 : "))
    flag = search(root, find_number)  # 입력 부분을 search 함수에서 제거
    print(f"{find_number}을(를) 찾았습니다." if flag else f"{find_number}이(가) 존재하지 않습니다.")

    delete_number = int(input("삭제할 값 입력 : "))
    # root = delete_right(root, delete_number)
    root = delete_left(root, delete_number)
    post_order(root)
    print()
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

