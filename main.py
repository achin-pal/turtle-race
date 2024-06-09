import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("give a bigge rnumber")
        quit()
else:
        print("give me a number next time")
        quit()

random_number=random.randint(0,top_of_range)
guesses=0;

while True:
    guesses += 1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("give me a number next time")
        continue

    if user_guess == random_number:
        print("got it")
        break
    else:
        if user_guess > random_number:
            print("above the number")
        else:
            print("below number")

print('got it in', guesses, "gueese")
