import random

# welcome the user
print('⚠️⚠️⚠️welcome to⚠️⚠️⚠️')
print('🌚𝓕𝓻𝓮𝓪𝓴𝔂 maths games🌚')


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == "y":
            return "yes"
        elif response == 'no' or response == "n":
            return "no"
        else:
            print('please enter yes / no')


# instructions for game
def instructions():
    print('''------in this 𝓕𝓻𝓮𝓪𝓴𝔂 math game you will be asked-------
  what game mode you want to use, how many questions 
 you want and you will be forced! to answer the given 
questions or else you will be punished by 𝓕𝓻𝓮𝓪𝓴𝔂 𝓑𝓸𝓫 👅''')


# Asks the user if they would like to see the instructions
want_instruction = yes_no('do you need instructions(I would recomend) ')

# checks for yes or no
if want_instruction == 'yes':
    instructions()

# giving an answer
ans: str = 'yes'

# asking if they understand
print('     ------do you understand the rules?------')
str = input('                     ')
if str == 'yes':

    # if they understand print this
    print('''
[easy], 
[normal], 
[𝓕𝓻𝓮𝓪𝓴𝔂]''')


else:
    print('Do you feel his presence')
    exit()


# checking for a gamemode
def question_difficulty(difficulty):
    diff = input(difficulty).lower()

    if diff == 'easy' or diff == 'e':
        return "easy"
    elif diff == 'normal' or diff == 'n':
        return "normal"
    elif diff == 'freaky' or diff == 'f' or diff == '𝓕𝓻𝓮𝓪𝓴𝔂':
        return "𝓕𝓻𝓮𝓪𝓴𝔂"
    else:
        print('please enter selected options ')


# asks them to select a gamemode
select_gameMode = question_difficulty('''select game mode
''')


# if freaky mode is selected do this
def freaky_modeStart():
    print('''
┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗ ┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏       
┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝ ┈╱╭▏╮╭┻┻╮╭┻┻╮╭
▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░ ▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏  
▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░ ▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏  
▕╭╮▏╮┈┈┈┈┏━━━╯▏░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ╭╮▏╮┈┈┈┈┏━━━╯▏
▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝ ▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏
▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏                                                                  ▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏
▕┈╰▏╰╯╰━━━━╯┈┈▏------------------you have 𝓕𝓻𝓮𝓪𝓴𝔂 mode selected------------------▕┈╰▏╰╯╰━━━━╯┈┈▏
               ''')

    game_history = []

    def input_to_number():
        user_input = input("How many questions: ")
        try:
            number = int(float(user_input))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    result = input_to_number()
    if result is not None:
        print('here is', result, 'questions')

    def generate_question():
        # generate a math question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}? "
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        return question, answer

    def quiz(num_questions):

        score = 0
        for _ in range(num_questions):
            question, correct_answer = generate_question()
            user_answer = input(question)
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    game_history.append((question, user_answer, "Correct"))
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")
                    game_history.append((question, user_answer, "Incorrect"))
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"You got {score} out of {num_questions} correct. {score / num_questions * 100}%")
        # Check if the percentage is over 80%
        if score / num_questions * 100 >= 80:
            print("since you did a good job, wanna get 𝓕𝓻𝓮𝓪𝓴𝔂 with bob")
        else:
            print('Get better lol')

        if input("Do you want to see game history? (yes/no): ").lower() == "yes":
            for i, (question, user_answer, result) in enumerate(game_history, start=1):
                print(f"Question {i}: {question} Your answer: {user_answer}, Result: {result}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            freaky_modeStart()
        else:
            print("Thank you for playing!")

        # number of questions

    quiz(result)


# if normal mode is selected do this
def normal_modeStart():
    print('''
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
------------------you have selected normal mode------------------''')

    game_history = []

    def input_to_number():
        user_input = input("How many questions: ")
        try:
            number = int(float(user_input))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    result = input_to_number()
    if result is not None:
        print('here is', result, 'questions')

    def generate_question():
        # generate a math question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}? "
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        return question, answer

    def quiz(num_questions):

        score = 0
        for _ in range(num_questions):
            question, correct_answer = generate_question()
            user_answer = input(question)
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    game_history.append((question, user_answer, "Correct"))
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")
                    game_history.append((question, user_answer, "Incorrect"))
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"You got {score} out of {num_questions} correct. {score / num_questions * 100}%")
        # Check if the percentage is over 80%
        if score / num_questions * 100 >= 80:
            print("nice job, bob?.")
        else:
            print('Get better lol')

        if input("Do you want to see game history? (yes/no): ").lower() == "yes":
            for i, (question, user_answer, result) in enumerate(game_history, start=1):
                print(f"Question {i}: {question} Your answer: {user_answer}, Result: {result}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            normal_modeStart()
        else:
            print("Thank you for playing!")

        # number of questions

    quiz(result)


# if easy mode is selected do this
def easy_modeStart():
    print('''
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
-------------------you have selected easy mode-------------------''')

    game_history = []

    def input_to_number():
        user_input = input("How many questions: ")
        try:
            number = int(float(user_input))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    result = input_to_number()
    if result is not None:
        print('here is', result, 'questions')

    def generate_question():
        # generate a math question
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}? "
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        return question, answer

    def quiz(num_questions):

        score = 0
        for _ in range(num_questions):
            question, correct_answer = generate_question()
            user_answer = input(question)
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    game_history.append((question, user_answer, "Correct"))
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")
                    game_history.append((question, user_answer, "Incorrect"))
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"You got {score} out of {num_questions} correct. {score / num_questions * 100}%")
        # Check if the percentage is over 80%
        if score / num_questions * 100 >= 80:
            print("good game.")
        else:
            print('Get better lol')

        if input("Do you want to see game history? (yes/no): ").lower() == "yes":
            for i, (question, user_answer, result) in enumerate(game_history, start=1):
                print(f"Question {i}: {question} Your answer: {user_answer}, Result: {result}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            easy_modeStart()
        else:
            print("Thank you for playing!")

        # number of questions

    quiz(result)


# if they selected one of these game modes then start that game mode
if select_gameMode == 'easy':
    easy_modeStart()

if select_gameMode == 'normal':
    normal_modeStart()

if select_gameMode == '𝓕𝓻𝓮𝓪𝓴𝔂':
    freaky_modeStart()
