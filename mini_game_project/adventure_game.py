name = input("TYPE YOUR NAME : ")
print("WELCOME", name, "TO THIS ADVENTURE")

answer = input(
    "YOU ARE ON THE DIRTY ROAD, IT HAS COME TO AN END AND YOU CAN GO LEFT OR RIGHT. WHICH WAY WOULD YOU LIKE TO GO ?  "
).upper()

if answer == "LEFT":
    answer = input("YOU COM TO A LIVER, YOU CAN WALK AROUND AND SWIM TO SWIM ACROSS")
    if answer == "SWIM":
        print()
    elif answer == "WALK":
        print()
    else:
        
elif answer == "RIGHT":
    print()
else:
    print("NOT A VALID OPTION. YOU LOSE !")

