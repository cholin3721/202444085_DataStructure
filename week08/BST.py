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


if __name__ == "__main__" :
    numbers = [10, 15, 8, 3, 9]

    node = TreeNode()
    node.data = numbers[0]
    root = node

    # 2번째 원소부터
    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root
        while True:
            if number < current.data :
                if current.left is None :
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None :
                    current.right = node
                    break
                current = current.right
    print("BST Structuring Complete")
    post_order(root)
    print()
    find_number = int(input())
    current = root

    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다.")
            break

        elif find_number < current.data:
            if current.left is None :
                print(f"{find_number}을(를) 찾을 수 없습니다.")
                break
            current = current.left

        else :
            if current.right is None :
                print(f"{find_number}을(를) 찾을 수 없습니다.")
                break
            current = current.right

        print("탐색 종료")