from collections import deque

# d = deque([17, 55, 123])  # 이렇게 넣어도 하나씩 다 들어감
d = deque((17, 55, 123))  # 이렇게 넣어도 하나씩 다 들어감
d.append((1,2))
d.appendleft(100)
d.append(7)
d.append(-91)
print(d.popleft())
print(d.popleft())

for _ in range(len(d)) :
    print(d.popleft())