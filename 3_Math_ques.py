import random
import time

operators = ["+", "-", "*"]
total_problems = 10

def generate_problem():
    left = random.randint(2, 20)
    right = random.randint(2, 20)
    operator = random.choice(operators)

    ques = str(left) + " " + operator + " " + str(right)  # Create the problem as a string
    answer = eval(ques)  # Evaluate the result
    return ques, answer  # Return both question and answer to be used in the main func later

wrong = 0
input("Press Enter to begin!")
print("-------------------------")

start_time = time.time()

# Main loop
for i in range(total_problems):
    ques, answer = generate_problem()  # Get question and answer

    while True:
        guess = int(input(f"Problem {i + 1}: {ques} = "))  # Ask the user for their answer
        if guess == answer:
            break
        else:
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("-------------------------")
print(f"Good Job! You finished in {total_time} seconds")