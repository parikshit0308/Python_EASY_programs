import random

number = input("Enter a number: ")

if  number.isdigit():
    number = int(number)

    if number  <= 0:
        print("Enter a number greater than zero")
        quit()
else:
    print("Please enter a number only")
    quit()

random_number = random.randint(0, number)

guesses = 0

while True:

    guesses += 1
    user_guess = input("Make a random guess: \n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number not any another format")
        continue

    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < random_number:
        print("Your guess is below number. Try again.\n")
    else:
        print("Your guess is above number. Try again.\n")

print("Your Guessed the number in",guesses,"guesses.")