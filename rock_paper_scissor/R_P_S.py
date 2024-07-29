import random

user_wins = 0
bot_wins = 0

select_options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissor) or q to quit: ").lower()
    if user_choice == "q":
        break

    if user_choice not in select_options:
        print("Invalid choice. Please try again.")
        continue

    random_number = random.randint(0 , 2)

    bot_choice = select_options[random_number]
    print("Bot picks: ", bot_choice + ".")

    if user_choice == "rock" and bot_choice == "scissors":
        print("You win!!🥳")
        user_wins += 1
    elif user_choice == "paper" and bot_choice == "rock":
        print("You win!!🥳")
        user_wins += 1 
    elif user_choice == "scissors" and bot_choice == "paper":
        print("You win!!🥳")
        user_wins += 1       
    else:
        print("Bot wins!!😒")
        bot_wins += 1   

print("You won: ", user_wins, "times")    
print("You won: ", bot_wins, "times")
print("Bye Bye!!!👋")

