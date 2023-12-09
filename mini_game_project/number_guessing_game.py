import random

top_range = input("TYPE A NUMBER : ")


if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0 :
        print("PLEASE TYPE A NUMBER LARGER THAN 0 NEXT TIME.")
        quit()

else :
    print("PLEASE TYPE A NUMBER NEXT TIME.")
    quit()

random_num = random.randint(0, top_range)

guess_count = 0

while True :
    guess_count += 1
    user_guess = input("MAKE A GUESS ! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else :
        print("PLEASE TYPE A NUMBER NEXT TIME.")
        continue

    if user_guess == random_num :
        print("YOU GOT IT RIGHT ! ")
        break
    elif user_guess > random_num:
        print("YOU WERE ABOVE THE NUMBER ! ")
    else :
        print("YOU WERE BELOW THE NUMBER ! ")

print("YOU GOT IT IN",guess_count,"GUESSES ! ")