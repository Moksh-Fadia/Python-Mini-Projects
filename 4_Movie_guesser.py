import random

movies = ["interstellar", "inception", "thor", "prestige", "avengers", "golmaal"]

chosen_movie = random.choice(movies)
movie_display = ["_" for i in chosen_movie]     # ['_', '_', '_', '_', '_', '_', '_', '_', '_']
attempts = 10

print("Welcome to the game!")

while attempts > 0 and "_" in movie_display:    # as long as attempts are remaining and there are _ spaces left
    print("\n" + ' '.join(movie_display))    # _ _ _ _ (ie. joins all the _ from the list seperated by a space)
    guess = input("Guess a letter: ").lower()

    if guess in chosen_movie:       # guess is a letter given by the user
        for index, letter in enumerate(chosen_movie):
            if letter == guess:         # letter means the letter which is at a particular index in the word
                movie_display[index] = guess        # reveal letter
    else:
        print("The letter dosen't appear in the word!")
        attempts -= 1


# Game Conclusion
if "_" not in movie_display:        # means if there is no _ space left (ie. entire word guessed)
    print("Congratulations! You guessed the movie!")
    print(' '.join(movie_display))      # joins all the letters of the movie seperated by a spacef
else:
    print(f"Sorry! You ran out of attempts. The movie was {chosen_movie}.")







