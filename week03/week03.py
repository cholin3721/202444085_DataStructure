import array
def move_zeroes(a_arr) :
    zero_index=0
    for i, n in enumerate(a_arr):
        if n!=0 :
            a_arr[zero_index] = n
            if i != zero_index:
                a_arr[i] = 0
            zero_index += 1
    return a_arr

def move_zeroes_v2(l):
    zero_idx = 0
    for i in range(len(l)):
        n=l[i]
        if n!= 0:
            l[zero_idx] = n
            if zero_idx != i:
                l[i] = 0
    return l

arr = array.array('i', [99, 0, -7, 0 , 16])
for i in range(len(arr)):
    print(f"{arr[i]:5}, {id(arr[i])}")


move_zeroes(arr)
print(arr)
# 파이썬은 같은 값은 shallow copy 얕은 복사를 통해 같은 데이터 같은 주소를 참조함

# l = [99, 99]
# print(id(0), id(1))  // 이건 좀 더 알아보기

# la = [99, 0, -7, 0, 16]
# for i in range (len(l)) :
#     print(f"{l[i]:3}, {id(l[i])}")