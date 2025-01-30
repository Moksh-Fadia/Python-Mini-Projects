import random

def roll():
    return random.randint(1, 6)  # Corrected dice range

while True:
    players = int(input("Enter no. of players (2-4): "))

    if 2 <= players <= 4:
        break
    else:
        print("Must be between 2-4 players")

max_score = 50
player_scores = [0 for i in range(players)]  # Initialize scores to 0

while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer number {player_index + 1}'s turn has started")
        print(f"Your total score is: {player_scores[player_index]}\n")

        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y or n): ")

            if should_roll.lower() == "y":  # Fixed method call
                value = roll()
                if value == 1:
                    print("Oops you rolled a 1! Your turn is done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}")
            else:
                break

            print(f"Your current score is: {current_score}")

        player_scores[player_index] += current_score
        print(f"Your total score is: {player_scores[player_index]}")

        # Check if the player has reached the maximum score
        if player_scores[player_index] >= max_score:
            break
    else:
        continue  # Only continue if the inner loop wasn't broken
    break  # Exit the outer loop if a winner is found

max_score = max(player_scores)
winning_index = player_scores.index(max_score)

print(f"Player number {winning_index + 1} is the winner with a score of {max_score}!")
