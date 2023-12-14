import random
print("What alphabet system has taken from these: ")
options = ["X", "Q", "F", "B", "Z", "K"]
print(options)

random_answer = random.choice(options)
user_attempts = 0
max_attempts = 3
while user_attempts < max_attempts:
    user_input = input("Enter the missing word: ").capitalize()
    user_attempts += 1

    if user_input == random_answer:
        print("You Guessed Correct!")
        print("You Won in " + str(user_attempts) + " attempts")
        break
    else:
        print("You guessed wrong. Try again.")

if user_attempts == max_attempts:
    print("Sorry, you've used all your attempts. The correct answer was:", random_answer)
