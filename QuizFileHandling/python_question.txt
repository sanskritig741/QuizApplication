import random
import os


USER_FILE = "users.txt"
RESULTS_FILE = "results.txt"
PYTHON_QUESTIONS_FILE = "python_questions.txt"
JAVA_QUESTIONS_FILE = "java_questions.txt"
CPP_QUESTIONS_FILE = "cpp_questions.txt"

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    return users


def save_user(username, password):
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")
        
        

def load_questions(filename):
    questions = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    question_text = parts[0]
                    choices = parts[1:4]
                    answer = parts[4]
                    questions.append({"question": question_text, "choices": choices, "answer": answer})
    return questions




def register(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users:
        print("Username already exists.")
    else:
        users[username] = password
        save_user(username, password)
        print("Registration successful!")

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Wrong details!")
        return None

def attempt_quiz(username):
    score = 0
    print("1. Python")
    print("2. Java")
    print("3. C++")
    choice = input("Choose a quiz (1/2/3): ")

    if choice == "1":
        print("Python quiz started.")
        questions = load_questions(PYTHON_QUESTIONS_FILE)
    elif choice == "2":
        print("Java quiz started.")
        questions = load_questions(JAVA_QUESTIONS_FILE)
    elif choice == "3":
        print("C++ quiz started.")
        questions = load_questions(CPP_QUESTIONS_FILE)
    else:
        print("Invalid choice.")
        return

    if questions:
        selected_questions = random.sample(questions, k=min(5, len(questions)))
        for idx, q in enumerate(selected_questions, start=1):
            print(f"Q{idx}: {q['question']}")
            for i, option in enumerate(q['choices'], start=1):
                print(f"{i}. {option}")
            try:
                answer = int(input("Choose the correct answer (1/2/3): "))
                if q['choices'][answer - 1] == q['answer']:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was '{q['answer']}'.\n")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number corresponding to the answer choices.\n")

        print(f"Your score: {score} out of {len(selected_questions)}")
        save_results(username, choice, score, len(selected_questions))
    else:
        print("No questions available for this quiz.")

def save_results(username, subject, score, total):
    with open(RESULTS_FILE, "a") as file:
        file.write(f"{username},{subject},{score}/{total}\n")

def main():
    users = load_users()
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")
        if choice == "1":
            register(users)
        elif choice == "2":
            user = login(users)
            if user:
                print("You can now attempt the quiz.")
        elif choice == "3":
            user = login(users)
            if user:
                attempt_quiz(user)
            else:
                print("Please log in to attempt the quiz.")
        elif choice == "4":
            print("Thank you for using the Quiz Application.")
            break
        else:
            print("Choose a correct option.")

main()