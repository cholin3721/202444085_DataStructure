import random as rd

answer = rd.randint(0, 100)
cnt = 0
flag = False
high = 100
low = 0

for i in range(7) :
    guess = (high + low) //2
    if guess > answer :
        print(f"{guess} is too high, try lower")
        high = guess

    elif guess < answer :
        print(f"{guess} is too low, try higher")
        low = guess

    else :
        flag = True
        break
    cnt += 1
    print(f"{7-cnt} times left, try your best!")
print()
if flag :
    print(f"Congratulation! You win! answer is {answer}")
else :
    print("fuckin loser")