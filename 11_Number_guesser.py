import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
print(f"Select a number between {lowest_num} and {highest_num}.")

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess < lowest_num and guess >highest_num:
        print("Number is out of range! Try again.")

    elif guess < answer:
        print("Tow Low! Try again.")

    elif guess > answer:
        print("Tow High! Try again.")    

    else:
        print(f"Correct! The answer was {answer}.")
        print(f"Number of guesses: {guesses}")
        break

