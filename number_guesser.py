import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
#isdigit basically checks whether the input is digit or not, if true then convert it into integer cause above
#input was in string only. 
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
#randint predicts any random number including the range given. (should assign initial value)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")

print("You got it in", guesses, "guesses!")