questions = [
    {
        "prompt": "Who is the leader of the Avengers?",
        "options": ["A. Iron Man", "B. Captain America", "C. Thor", "D. Black Widow"],
        "answer": "B"
    },
    {
        "prompt": "What is the real name of Spider-Man?",
        "options": ["A. Peter Parker", "B. Tony Stark", "C. Steve Rogers", "D. Bruce Banner"],
        "answer": "A"
    },
    {
        "prompt": "What is the name of Thor's hammer?",
        "options": ["A. Stormbreaker", "B. Gungnir", "C. Mjolnir", "D. Excalibur"],
        "answer": "C"
    },
    {
        "prompt": "Which Infinity Stone does Vision have?",
        "options": ["A. Time Stone", "B. Mind Stone", "C. Power Stone", "D. Soul Stone"],
        "answer": "B"
    },
    {
        "prompt": "What is Black Panther's home country?",
        "options": ["A. Wakanda", "B. Sokovia", "C. Asgard", "D. Latveria"],
        "answer": "A"
    },
    {
        "prompt": "Who is Tony Stark's AI assistant?",
        "options": ["A. JARVIS", "B. FRIDAY", "C. EDITH", "D. KAREN"],
        "answer": "A"
    },
    {
        "prompt": "What is the Hulk's real name?",
        "options": ["A. Steve Rogers", "B. Clint Barton", "C. Bruce Banner", "D. Scott Lang"],
        "answer": "C"
    },
    {
        "prompt": "Which superhero uses the shield made of Vibranium?",
        "options": ["A. Iron Man", "B. Black Widow", "C. Hawkeye", "D. Captain America"],
        "answer": "D"
    },
    {
        "prompt": "Who is the villain in the first Avengers movie?",
        "options": ["A. Thanos", "B. Loki", "C. Ultron", "D. Red Skull"],
        "answer": "B"
    },
    {
        "prompt": "What is the name of Star-Lord's spaceship?",
        "options": ["A. Milano", "B. Benatar", "C. Dark Aster", "D. Sanctuary"],
        "answer": "A"
    }
]

score = 0

for question in questions:
    print(question["prompt"])       # prints each ques ka prompt
    for option in question["options"]:      # prints option of each question
        print(option)

    answer = input("Enter your answer (A, B, C or D): ").upper()
    if answer == question["answer"]:
        print("Correct! Good Job!\n")
        score += 1
    else:
        print("Oops! You answer is wrong!\n")

print(f"You got {score} out of {len(questions)} questions correct.")