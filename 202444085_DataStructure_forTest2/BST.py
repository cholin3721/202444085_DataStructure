class TreeNode :
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

def insert(root, value) :
    if root is None :
        insert_node = TreeNode()
        insert_node.value = value
        return insert_node
    if root.value > value :
        root.left = insert(root.left, value)
    elif root.value < value :
        root.right = insert(root.right, value)
    else :
        return root
    return root

def insert_ver2(root, value) :
    insert_node = TreeNode()
    insert_node.value = value
    if root is None :
        root = insert_node
        return root
    current = root
    while True :
        if current.value > value :
            if current.left is None :
                current.left = insert_node
                return root
            else :
                current = current.left
                continue
        elif current.value < value :
            if current.right is None :
                current.right = insert_node
                return root
            else :
                current = current.right
                continue
        else :
            return root
visited = list()
def post_order(root) :
    if root is None :
        return
    post_order(root.left)
    post_order(root.right)
    visited.append(root.value)

def search(root, value):
    current = root
    while current is not None:
        if current.value > value:
            current = current.left
        elif current.value < value:
            current = current.right
        else:
            return True
    return False

def search_ver2(root, value):
    global visited
    visited = list()
    post_order(root, value)
    return True if value in visited else False

def delete_left(root, value) :
    if root is None :
        return False
    if root.value < value :
        delete_left(root.right, value)
    elif root.value > value:
        delete_left(root.left, value)
    else :
        if root.left is None :
            root = root.right
            return
        elif root.right is None :
            root = root.left
            return
        else :
            current = root.left
            while current is not None :
                current = current.right
            root.value = current.value
            current = None
