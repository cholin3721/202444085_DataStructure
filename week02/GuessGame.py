import random as rd

answer = rd.randint(0,100)
cnt = 0
flag = False
high = 100
low = 0

while cnt < 7 :
    print(f"recommand pick : {(high + low) // 2}")
    guess = int(input("Guess the Number : "))

    if guess < answer :
        print(f"Guess is Low, Answer is Bigger")
        low = guess

    elif guess > answer :
        print(f"Guess is High, Answer is Lower")
        high = guess

    else :
        print(f"Congratulation!! You are Winner")
        flag = True
        break
    cnt+=1
    t = 7 - cnt
    print("1 time left" if t == 1 else f"{t} times left\n")
#    print(f"{7-cnt}" + "time" if 7-cnt == 1 else "times" + "left")

if flag == False :
    print("Loser")

