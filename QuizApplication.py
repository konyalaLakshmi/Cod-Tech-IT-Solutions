# Define questions, choices, and answers
questions = [
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["A. Elephant", "B. Blue whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "choices": ["A. China", "B. South Korea", "C. Japan", "D. Vietnam"],
        "answer": "C"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "choices": ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Lhotse"],
        "answer": "A"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choices": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Australia?",
        "choices": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"],
        "answer": "B"
    }
]

# Function to ask questions and calculate score
def quiz(questions):
    score = 0
    for question_data in questions:
        print(question_data["question"])
        for choice in question_data["choices"]:
            print(choice)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == question_data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question_data['answer']}.\n")
    return score

# Main program
print("Welcome to the Quiz!\n")
print("Please select the correct option for each question:\n")
user_score = quiz(questions)
print(f"Quiz completed! Your score is: {user_score}/{len(questions)}")
if user_score == len(questions):
    print("Congratulations, you got a perfect score!")
elif user_score >= len(questions) / 2:
    print("Well done, you did a good job!")
else:
    print("You can do better next time. Keep practicing!")
