def quiz_game():
    """A simple quiz game."""

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Rome"],
            "answer": "Paris",
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars",
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "answer": "Blue Whale",
        },
        {
          "question": "What is 2+2?",
          "options": ["3", "4", "5", "6"],
          "answer": "4"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "NaCl", "O2"],
            "answer": "H2O",
        },
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")

        while True: #input validation loop
          try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
          except ValueError:
            print("Invalid input. Please enter a number.")

        if q["options"][choice - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['answer']}")

    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()