import array

c = array.array('i', [1, 2, 3, 4, 5])

for i in c :
    print(i, id(i))

def move_zeroes(l) :
    zero_idx = 0
    for i, num in enumerate(l) :
        if num != 0 :
            l[zero_idx] = num
            if zero_idx != i :
                l[i] = 0
            zero_idx += 1
    return l
u1 = [1, 0, 2, 3, 0, 4, 10, 5, 0]
print(move_zeroes(u1))

def duplicate_numbers(l) :
    result_list= list()
    s = set()
    for data in l :
        length1 = len(s)
        s.add(data)
        length2 = len(s)
        if length1 == length2 :
            result_list.append(data)
    return result_list

u2 = [12,23,43,123,12,12,12,12,23,34,45,56,43,123]
print(duplicate_numbers(u2))

def inters(l1, l2) :
    l3 = list()
    for i in l1 :
        if i in l2 :
            l3.append(i)
    return l3

u3 = [1, 2, 3, 4]
u4 = [3, 4, 5, 6, 7]
print(inters(u3, u4))
print(set(u3) & set(u4))
print(set(u3).intersection(u4))  # 강제로 set을 바꿈

