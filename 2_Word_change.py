with open("story.txt", "r") as f:
    story = f.read()

words = set()   # we use set instead of list so that there are no duplicate <words>
start_of_word = -1

for i, char in enumerate(story):
    if char == "<":
        start_of_word = i

    if char == ">" and start_of_word != -1:
        word = story[start_of_word : i + 1]     # slicing of that word from its starting pstn to i+1
        words.add(word)     # add the sliced words ie. <word> in the set named words
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer       # dictionary[key] = value

for word in words:
    story = story.replace(word, answers[word])

print(story)    