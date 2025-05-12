def is_queue_full() -> bool:
    global SIZE, rear, front
    if rear != SIZE-1:
        return False
    elif rear == SIZE-1 and front == -1:
        return True
    else :
        for i in range(front+1, SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front = front - 1
        rear = rear - 1
        return False

# 꽉차 있을때 말곤 땡겨지지 않는다?


def is_queue_empty() -> bool:
    global SIZE, rear
    if rear == front:
        return True
    else :
        return False

def en_queue(data : object) :
    global rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return None
    rear = rear + 1
    queue[rear] = data

def de_queue() :
    global front
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = front + 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global front
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

SIZE = int(input("큐 사이즈 입력 : "))
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

if __name__ == "__main__":
    while True :
        menu = input("1. 삽입(i), 2. 추출(e), 확인(v), 종료(x) : ")
        if menu.upper() == "X" :
            print("프로그램을 종료합니다.")
            break
        elif menu.upper() == "I" :
            en_queue(input("입력할 데이터 : "))
            print(queue)
        elif menu.upper() == "E" :
            print(f"확인된 데이터 {de_queue()}")
            print(queue)
        else :
            print(f"{menu} 메뉴는 존재하지 않습니다. 메뉴의 기능을 이용해 주세요")