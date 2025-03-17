# alt + shift + f10
n = int(input("Input the Integer : "))
# result = 0
# for i in range(n+1) :
#     result = result + i  # O(n) 선형 시간을 가짐
result = n * (n+1) // 2  # O(1) 상수 시간을 가짐
print(result)


