import random

user_win = 0
cpu_win = 0

option = ["ROCK", "PAPER", "SCISSORS"]

while True:
    user_input = input("TYPE : ROCK / PAPER / SCISSORS // Q TO QUIT : ").upper()
    if user_input == "Q":
        break
    
    if user_input not in option :
        continue

    random_num = random.randint(0, 2)

    cpu_pick = option[random_num]
    print("COMPUTER PICKED :",cpu_pick + ".")

    if user_input == "ROCK" and cpu_pick == "SCISSORS":
        print("YOU WON ! ")
        user_win += 1
        continue
    elif user_input == "PAPER" and cpu_pick == "ROCK":
        print("YOU WON ! ")
        user_win += 1
        continue
    elif user_input == "SCISSORS" and cpu_pick == "PAPER":
        print("YOU WON ! ")
        user_win += 1
        continue
    else :
        print("YOU LOST ! ")
        cpu_win += 1

print("YOU WON", user_win, "TIMES ! ")
print("COMPUTER WON", cpu_win, "TIMES ! ")
print("GOOD BYE ! ")