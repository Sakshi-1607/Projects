# Quiz Application

# Questions and answers
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Bihar", "B. kolkata", "C. Dalhi", "D. Goa"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Blue Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "A"
    },
    {
        "question": "Who is the first Prime Minister of India?",
        "options": ["A. Pt. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Balabh bhai patel", "D. Indira gandhi"],
        "answer": "A"
    },
    {
        "question": "Who is the first president of india?",
        "options": ["A. Mahatma Gandhi", "B. Dr.Rajendra prashad", "C.Pt. Jawaharlal Nehru ", "D. Indira gandhi"],
        "answer": "B"
    },
    {
        "question": "How many states are there in India?",
        "options": ["A. 36", "B. 29", "C. 13", "D. 12"],
        "answer": "B"
    }
]

score = 0

for i, q in enumerate(quiz):
    print(f"\nQuestion {i + 1}: {q['question']}")
    for option in q['options']:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}")

# Final Score
print(f"\nYour final score is: {score}/{len(quiz)}")
