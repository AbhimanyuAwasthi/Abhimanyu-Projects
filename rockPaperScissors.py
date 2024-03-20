from random import randint

user_score = 0
py_score = 0

print("Hello There!")
question = input("Would you like to play a game of 'Rock, Paper, Scissoors' with me? [y/n] ")

while question.lower() != 'n':
    if question.lower() == 'y':
        random_number = randint(1, 3)

        choice = input("What do you choose, Rock, Paper or Scissors? [r/p/s] ")

        if choice.lower() == 'r' and random_number == 1:
            print("I have chosen rock. We have chosen the same thing.")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'r' and random_number == 2:
            py_score += 1
            print("I have chosen paper. You lost!")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'r' and random_number == 3:
            user_score += 1
            print("I have chosen scissors. You won!")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")

        elif choice.lower() == 'p' and random_number == 1:
            user_score += 1
            print("I have chosen rock. You won!")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'p' and random_number == 2:
            print("I have chosen paper. We have chosen the same thing")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'p' and random_number == 3:
            py_score += 1
            print("I have chosen scissors. You lost!")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")


        elif choice.lower() == 's' and random_number == 1:
            py_score += 1
            print("I have chosen rock. You lost!")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 's' and random_number == 2:
            user_score += 1
            print("I have chosen paper. You won!")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 's' and random_number == 3:
            print("I have chosen scissors. We have chosen the same thing.")
            print(f"Your Score: {user_score}")
            print(f"My score: {py_score}")
            question = input("Would you like to play again? [y/n] ")

        else:
            print("Invalid input. Please type 'r', 'p', 's'")

    else:
        print("Invalid input. Please type 'y' or 'n'")
        question = input("Would you play again? [y/n] ")

print("Good-bye!")
user_score = 0
py_score = 0
