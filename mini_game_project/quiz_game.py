print("!!!Welcome to my computer quiz!!!")

playing = input("DO YOU WANT TO PLAY ? ").upper()

if playing != "YES" :
    quit()

print("OKAY LET'S PLAY !")

score = 0

answer1 = input("WHAT DOES CPU STAND FOR ? ").lower()
if answer1 == "central processing unit" :
    print("CORRECT ! ")
    score += 1
else :
    print("INCORRECT ! ")

answer2 = input("WHAT DOES GPU STAND FOR ? ").lower()
if answer2 == "graphics processing unit" :
    print("CORRECT ! ")
    score += 1
else :
    print("INCORRECT ! ")

answer3 = input("WHAT DOES RAM STAND FOR ? ").lower()
if answer3 == "random access memory" :
    print("CORRECT ! ")
    score += 1
else :
    print("INCORRECT ! ")

answer4 = input("WHAT DOES PSU STAND FOR ? ").lower()
if answer4 == "power supply" :
    print("CORRECT ! ")
    score += 1
else :
    print("INCORRECT ! ")

print("YOU GOT " + str(score) + " QUESTIONS CORRECT ! ")
print("YOU GOT " + str((score)/4 * 100) + " % QUESTIONS CORRECT ! ")