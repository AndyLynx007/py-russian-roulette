import random
pos_b = random.randint(0,5)
pos_p = 0

print("Russian Roulette by AndyLynx007")
start = input("Press enter to start:")

while quit != "q":
    if pos_p == pos_b:
        print("bang")
        input("ur ded :(")
        break
    elif pos_p != pos_b:
        print("click")
        pos_p += 1
        if pos_p > 5:
            pos_p = 0
        quit = input("again?")