import random
import mysql.connector
from getpass import getpass


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),  
    database="QuizApp"
)

cursor = db.cursor(dictionary=True)


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
    if cursor.fetchone():
        print("Username already exists.")
    else:
        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        return user['user_id']
    else:
        print("Wrong details!")
        return None


def load_questions(subject):
    cursor.execute("SELECT * FROM Questions WHERE subject = %s", (subject,))
    return cursor.fetchall()

def attempt_quiz(user_id):
    print("1. Python")
    print("2. Java")
    print("3. C++")
    choice = input("Choose a quiz (1/2/3): ")

    subject_map = {"1": "Python", "2": "Java", "3": "C++"}
    subject = subject_map.get(choice)
    if not subject:
        print("Invalid choice.")
        return

    print(f"{subject} quiz started.")
    questions = load_questions(subject)
    if not questions:
        print(f"No questions available for {subject} quiz.")
        return

    selected_questions = random.sample(questions, k=min(5, len(questions)))
    score = 0
    for idx, q in enumerate(selected_questions, start=1):
        print(f"Q{idx}: {q['question_text']}")
        print(f"1. {q['choice1']}")
        print(f"2. {q['choice2']}")
        print(f"3. {q['choice3']}")
        try:
            answer = int(input("Choose the correct answer (1/2/3): "))
            if q[f"choice{answer}"] == q['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was '{q['correct_answer']}'.\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to the answer choices.\n")

    print(f"Your score: {score} out of {len(selected_questions)}")
    save_results(user_id, subject, score, len(selected_questions))

def save_results(user_id, subject, score, total):
    cursor.execute(
        "INSERT INTO Results (user_id, subject, score, total) VALUES (%s, %s, %s, %s)",
        (user_id, subject, score, total)
    )
    db.commit()
    print("Results saved successfully!")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                print("You can now attempt the quiz.")
        elif choice == "3":
            user_id = login()
            if user_id:
                attempt_quiz(user_id)
            else:
                print("Please log in to attempt the quiz.")
        elif choice == "4":
            print("Thank you for using the Quiz Application.")
            break
        else:
            print("Choose a correct option.")

if __name__ == "__main__":
    main()