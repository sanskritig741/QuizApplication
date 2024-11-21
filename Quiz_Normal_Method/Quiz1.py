import random

users={}
python_question = [
    {"question": "What is the output of print(2 * 3)", "choices": ["5", "6", "8"], "answer": "6"},
    {"question": "Which keyword is used to define a function in Python?", "choices": ["def", "func", "lambda"], "answer": "def"},
    {"question": "What is the result of 10 // 3 in Python?", "choices": ["3", "3.33", "None"], "answer": "3"},
    {"question": "Which of these data types is immutable?", "choices": ["list", "dict", "tuple"], "answer": "tuple"},
    {"question": "How do you start a comment in Python?", "choices": ["//", "/*", "#"], "answer": "#"},
    {"question": "What does 'len()' function return?", "choices": ["Length of a list", "Sum of elements", "None"], "answer": "Length of a list"},
    {"question": "What is the correct file extension for Python files?", "choices": [".py", ".java", ".txt"], "answer": ".py"},
    {"question": "Which function is used to get user input in Python?", "choices": ["input()", "scanf()", "cin>>"], "answer": "input()"},
    {"question": "What is the output of print(10 % 3)?", "choices": ["3", "1", "0"], "answer": "1"},
    {"question": "How do you start a for loop in Python?", "choices": ["for (i = 0; i < 5; i++)", "for i in range(5)", "foreach(i : range)"], "answer": "for i in range(5)"},
    {"question": "What does the 'break' statement do?", "choices": ["Stops the loop", "Skips an iteration", "Continues the loop"], "answer": "Stops the loop"},
    {"question": "Which of the following is a mutable data type?", "choices": ["list", "tuple", "str"], "answer": "list"},
    {"question": "How do you import a module in Python?", "choices": ["import module_name", "include module_name", "module module_name"], "answer": "import module_name"},
    {"question": "What does 'append()' do in a list?", "choices": ["Adds an item to the end", "Removes an item", "Sorts the list"], "answer": "Adds an item to the end"},
    {"question": "Which keyword is used to create a class in Python?", "choices": ["class", "def", "struct"], "answer": "class"},
    {"question": "How do you create an empty dictionary?", "choices": ["{}", "[]", "()"], "answer": "{}"},
    {"question": "What is the output of bool([]) in Python?", "choices": ["True", "False", "Error"], "answer": "False"},
    {"question": "Which function is used to convert a string to lowercase?", "choices": ["toLower()", "lower()", "str.lower()"], "answer": "lower()"},
    {"question": "What does 'None' represent in Python?", "choices": ["An integer", "A string", "The absence of a value"], "answer": "The absence of a value"},
    {"question": "What will '3 ** 2' evaluate to?", "choices": ["6", "9", "None"], "answer": "9"},
]
java_question = [
     {"question": "Which keyword is used to declare a class in Java?", "choices": ["class", "Class", "struct"], "answer": "class"},
    {"question": "Which symbol is used to import a package in Java?", "choices": ["#", "@", "import"], "answer": "import"},
    {"question": "Which data type is used to create a variable that should store text in Java?", "choices": ["String", "Text", "Char"], "answer": "String"},
    {"question": "What is the correct way to create an object in Java?", "choices": ["MyClass obj = new MyClass();", "MyClass obj();", "obj MyClass = new MyClass();"], "answer": "MyClass obj = new MyClass();"},
    {"question": "How do you declare a main method in Java?", "choices": ["void main()", "public static void main(String[] args)", "main()"], "answer": "public static void main(String[] args)"},
    {"question": "What is the correct extension for Java files?", "choices": [".java", ".js", ".txt"], "answer": ".java"},
    {"question": "Which symbol is used to inherit a class in Java?", "choices": ["extends", "inherits", "implements"], "answer": "extends"},
    {"question": "What is the output of '10 % 3' in Java?", "choices": ["1", "3", "0"], "answer": "1"},
    {"question": "Which Java keyword is used to make a variable constant?", "choices": ["constant", "final", "const"], "answer": "final"},
    {"question": "How do you write a single-line comment in Java?", "choices": ["//", "#", "/*"], "answer": "//"},
    {"question": "Which function is used to output text in Java?", "choices": ["System.out.print", "console.log", "cout"], "answer": "System.out.print"},
    {"question": "How do you create a new instance of a class in Java?", "choices": ["new ClassName()", "ClassName.create()", "ClassName instance"], "answer": "new ClassName()"},
    {"question": "What does the 'this' keyword refer to in Java?", "choices": ["The current class", "The current object", "A parent class"], "answer": "The current object"},
    {"question": "What is the root class of all classes in Java?", "choices": ["Main", "Object", "Root"], "answer": "Object"},
    {"question": "Which Java keyword is used to handle exceptions?", "choices": ["try", "catch", "finally"], "answer": "try"},
    {"question": "How is a multi-line comment written in Java?", "choices": ["/* comment */", "# comment #", "// comment //"], "answer": "/* comment */"},
    {"question": "Which keyword is used to return a value from a method in Java?", "choices": ["return", "output", "result"], "answer": "return"},
    {"question": "Which access modifier allows visibility within the same package?", "choices": ["public", "protected", "default"], "answer": "default"},
    {"question": "How do you define an interface in Java?", "choices": ["interface", "abstract class", "protocol"], "answer": "interface"},
    {"question": "What is the keyword to define an enumeration in Java?", "choices": ["enum", "enumeration", "enumtype"], "answer": "enum"},
    
]    
cpp_question =  [
     {"question": "Which operator is used to access the address of a variable in C++?", "choices": ["*", "&", "#"], "answer": "&"},
    {"question": "Which function is used to output data to the console in C++?", "choices": ["cout", "print", "console"], "answer": "cout"},
    {"question": "What is the correct syntax to include a library in C++?", "choices": ["#include <library>", "import library", "include library"], "answer": "#include <library>"},
    {"question": "Which of the following is the entry point of a C++ program?", "choices": ["main", "start", "void"], "answer": "main"},
    {"question": "Which operator is used for dereferencing pointers in C++?", "choices": ["&", "*", "->"], "answer": "*"},
    {"question": "What is the correct file extension for C++ files?", "choices": [".cpp", ".c", ".hpp"], "answer": ".cpp"},
    {"question": "Which keyword is used to define constants in C++?", "choices": ["const", "constant", "immutable"], "answer": "const"},
    {"question": "How do you define a pointer in C++?", "choices": ["int *p;", "int p;", "int ptr;"], "answer": "int *p;"},
    {"question": "Which loop structure is NOT available in C++?", "choices": ["foreach", "for", "do-while"], "answer": "foreach"},
    {"question": "What does the 'new' keyword do in C++?", "choices": ["Allocates memory", "Creates a function", "Returns a pointer"], "answer": "Allocates memory"},
    {"question": "What does the delete keyword do in C++?", "choices": ["Releases memory", "Deletes a variable", "Removes a pointer"], "answer": "Releases memory"},
    {"question": "How do you declare a reference variable in C++?", "choices": ["int &ref", "int ref", "&int ref"], "answer": "int &ref"},
    {"question": "Which keyword is used for inheritance in C++?", "choices": ["extends", "inherits", "public"], "answer": "public"},
    {"question": "How do you access a member of a structure in C++?", "choices": [".", "->", "*"], "answer": "."},
    {"question": "What does 'NULL' represent in C++?", "choices": ["An integer", "A character", "The absence of a value"], "answer": "The absence of a value"},
    {"question": "What is the size of an int in C++?", "choices": ["2 bytes", "4 bytes", "8 bytes"], "answer": "4 bytes"},
    {"question": "What is the scope resolution operator in C++?", "choices": ["::", ".", "->"], "answer": "::"},
    {"question": "Which of these is NOT a built-in data type in C++?", "choices": ["int", "float", "decimal"], "answer": "decimal"},
    {"question": "How do you declare a template in C++?", "choices": ["template <class T>", "class template<T>", "type T"], "answer": "template <class T>"},
    {"question": "What is the use of 'inline' in C++?", "choices": ["Optimize function calls", "Define a class", "Access private data"], "answer": "Optimize function calls"},
]



def register():
    username = input("Enter your username:")
    password = input("Enter your password:")
    if username in users:
        print("Username already exist.")
    else:    
        users[username] = password
        print("Registration successful!")



def login():
    username = input("Enter your username:")
    password = input("Enter your password:")
    if users.get(username) == password:
        print("Login successful")
    else:
        print("Wrong details!")
        
        
def attempt_quiz():
    score = 0
    while True:
        print("1.Python")
        print("2.Java")
        print("3.c++")
        choices = input("choose option (1/2/3):")
        if choices == "1":
            print("python quiz started")
            questions = random.sample(python_question,k=5)
        elif choices == "2":
            print("java quiz started")
            questions = random.sample(java_question,k=5)
        elif choices == "3":
            print("c++ quiz started")
            questions = random.sample(cpp_question,k=5)    
        else:
            print("choose correct option")
        for idx, q in enumerate(questions, start=1):
            print(f"Q{idx}: {q['question']}")
            for i, choice in enumerate(q['choices'], start=1):
                print(f"{i}. {choice}")
            answer = input("Choose the correct answer (1/2/3): ")

       
        if q['choices'][int(answer) - 1] == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
        print(f"Your score: {score} out of 5\n") 





def main():
    while True:
        print("1.Registration")
        print("2.Login")
        print("3.Attempt quiz")
        print("4.Exit")
        choice = input("choose option (1/2/3/4):")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":        
            attempt_quiz()
        elif choice == "4":
            print("Thank you for using the Quiz Application.")
            break
        else:
            print("choose correct option")


main()        