# TEAM ASSIGNMENT OF VALORANT
# Copyright © 2020 Asto_nish. All rights reserved.

import random
import os

os.system("cls")
slash = "//////////////////////////////"
# TEAM ATT, TEAM BLUE, SPECTATOR
attack, defend, spectator = [], [], []

print("空白区切りでユーザーネームを入力してください(例:1 2 3 4 5...)")
while 1:
    try:
        userlist = input().split()
        a = len(userlist)
        if a > 12:
            print("人数が多いようです もう一度入力してください")
        elif a == 0:
            print("名前が入力されていません もう一度入力してください")
        else:
            break
    except Exception as e:
        print("エラーです もう一度入力してください :", e)

# userlist = "1 2 3 4 5 6 7 8 9 10 11 12".split()

a = len(userlist)
b = 0
r = random.sample(range(a), a)

for i, r in enumerate(r):
    if a <= 10:
        if i - b <= a // 2 - 1:
            attack.append(userlist[r])
        else:
            defend.append(userlist[r])
    else:
        a -= 1
        b += 1
        spectator.append(userlist[r])

c = random.randint(0, 2)
if c == 1:
    attack, defend = defend, attack

os.system("cls")

if not spectator:
    print(
        "{} \nTEAM ORANGE : {} \nTEAM BLUE : {} \n{}".format(
            slash, " / ".join(attack), " / ".join(defend), slash
        )
    )
else:
    print(
        "{} \nTEAM ORANGE : {} \nTEAM BLUE : {} \nTEAM SPECTATOR : {}\n{}".format(
            slash, " / ".join(attack), " / ".join(defend), " / ".join(spectator), slash
        )
    )

