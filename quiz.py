# Dummy database for users
users_db = {}

# Quiz questions for different sections (10 questions per section)
quiz_sections = {
    "Science": [
        ("What planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "2"),
        ("What is the chemical symbol for water?", ["O2", "H2O", "CO2", "NaCl"], "2"),
        ("What gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "3"),
        ("What is the speed of light in m/s?", ["300000", "299792458", "150000", "100000"], "2"),
        ("Which organ purifies our blood?", ["Heart", "Kidney", "Lungs", "Liver"], "2"),
        ("What is the atomic number of hydrogen?", ["1", "2", "3", "4"], "1"),
        ("Who proposed the theory of relativity?", ["Newton", "Einstein", "Galileo", "Tesla"], "2"),
        ("What is the boiling point of water in Celsius?", ["0", "50", "100", "200"], "3"),
        ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], "3"),
        ("What is the chemical symbol for gold?", ["Au", "Ag", "Pb", "Fe"], "1"),
    ],
    "Mathematics": [
        ("What is 2 + 2?", ["3", "4", "5", "6"], "2"),
        ("What is the square root of 64?", ["6", "7", "8", "9"], "3"),
        ("What is 5 factorial (5!)?", ["60", "120", "24", "20"], "2"),
        ("What is 10% of 200?", ["20", "30", "40", "50"], "1"),
        ("What is the value of pi (approx)?", ["3.14", "3.15", "3.16", "3.17"], "1"),
        ("What is the formula for area of a circle?", ["pi*r^2", "2*pi*r", "pi*r", "r^2"], "1"),
        ("What is 7 * 8?", ["54", "56", "58", "60"], "2"),
        ("What is 100 divided by 4?", ["20", "25", "30", "40"], "2"),
        ("What is 12 squared?", ["120", "140", "144", "150"], "3"),
        ("What is the sum of angles in a triangle?", ["180", "270", "360", "90"], "1"),
    ],
    "History": [
        ("Who was the first President of the United States?", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "2"),
        ("What year did World War II end?", ["1942", "1945", "1947", "1950"], "2"),
        ("Who discovered America?", ["Christopher Columbus", "Leif Erikson", "Amerigo Vespucci", "James Cook"], "1"),
        ("Which empire was ruled by Julius Caesar?", ["Roman", "Ottoman", "Mongol", "Byzantine"], "1"),
        ("When was the Declaration of Independence signed?", ["1775", "1776", "1777", "1778"], "2"),
        ("Who was the first man to walk on the moon?", ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "2"),
        ("In which year was the Berlin Wall taken down?", ["1985", "1989", "1991", "1995"], "2"),
        ("Who was known as the Iron Lady?", ["Margaret Thatcher", "Angela Merkel", "Indira Gandhi", "Golda Meir"], "1"),
        ("Which ancient civilization built the pyramids?", ["Mayans", "Egyptians", "Romans", "Greeks"], "2"),
        ("What was the capital of the Byzantine Empire?", ["Rome", "Athens", "Constantinople", "Cairo"], "3"),
    ],
}

def register():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Try logging in.")
        return
    password = input("Enter a password: ")
    users_db[username] = password
    print("Registration successful! You can now log in.")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def start_quiz(section):
    print(f"\n--- {section} Quiz ---")
    score = 0
    questions = quiz_sections[section]
    for i, (question, options, correct_answer) in enumerate(questions, 1):
        print(f"\nQ{i}. {question}")
        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")
        answer = input("Enter the number of your answer: ")
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    print(f"\nQuiz Completed! Your score: {score}/{len(questions)}")
    return score

def main():
    print("Welcome to the Quiz App!")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\nChoose a quiz section:")
                    for i, section in enumerate(quiz_sections.keys(), 1):
                        print(f"{i}. {section}")
                    print("4. Logout")
                    section_choice = input("Enter your choice: ")
                    if section_choice in ["1", "2", "3"]:
                        section = list(quiz_sections.keys())[int(section_choice) - 1]
                        start_quiz(section)
                    elif section_choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
