SIZE = int(input("큐 사이즈 입력 : "))
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

def is_queue_full() -> bool :
    global SIZE, rear, front, queue
    if rear != SIZE -1 :
        return False
    elif front != -1 and rear == SIZE -1 :
        for i in range(1, len(queue)) :
            queue[i-1] = queue[i]
            queue[i] = None
        rear -= 1
        front -= 1
        return False
    else :
        return True

def is_queue_empty() -> bool :
    global SIZE, rear, front, queue
    if rear == front:
        return True
    else :
        return False

def enqueue(value : object) -> bool :
    global SIZE, rear, front, queue
    if is_queue_full() :
        return False
    else :
        rear += 1
        queue[rear] = value
        return True

def dequeue() -> object :
    global SIZE, rear, front, queue
    if is_queue_empty() :
        return None
    else :
        front += 1
        data = queue[front]
        queue[front] = None
        return data

if __name__ == "__main__" :

