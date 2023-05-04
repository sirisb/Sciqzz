"""
Create a Science Quiz.
Once User starts quiz, maintain scoring. After user crosses certain score, turn the quiz to adaptive.
100 points wins the game. Loosing on a question once stays in same level, but loosing twice automatically
lowers level and throws comparatively easier question. 2 right answers in a row increases the difficulty
level and so the points.
"""
import csv
import sys
import random
import pyfiglet


def shuffle_all_level_list(level_list_dict):
    for key in level_list_dict.keys():
        random.shuffle(level_list_dict[key])
        # print(f"{key} %%%%% ", len(level_list_dict[key]))


def read_csv(quiz_data_file, level_list_dict):
    q_list = []
    try:
        with open(quiz_data_file) as q_file:
            reader = csv.DictReader(q_file)
            keys = reader.fieldnames
            # print(keys)
            for row in reader:
                q_record = {}
                for key in keys:
                    if key == "points":
                        q_list = level_list_dict[get_level_list(int(row[key]))]
                    q_record[key] = row[key]
                q_list.append(q_record)
                # print(q_list)
    except FileNotFoundError:
        sys.exit("Quiz data file not found!")
    except KeyError:
        sys.exit("Key not found in CSV")
    else:
        shuffle_all_level_list(level_list_dict)
        # random.shuffle(q_list)  # shuffle the list to throw questions in random order everytime to the user.
        # return q_list # declared as global variable, so no return required.


def get_level_list(points):
    if points <= 5:
        return "easy"
    if 5 < points <= 10:
        return "medium"
    if points > 10:
        return "hard"


def begin_quiz(quiz_data_file):
    # load CSV
    # if score > prev_score & score - prev_score > 10, level up to new weight problem, else same weight problem.
    # show if the q_num is not present in dict  ONLY.
    # store all asked q_nums in a dict.
    # 3 fails in a row will terminate the quiz.
    fails = 0
    score = 0
    level_list_dict = {"easy": [], "medium": [], "hard": []}
    # read quiz data file to a tuple of list with dict.
    read_csv(quiz_data_file, level_list_dict)
    for q_level in level_list_dict:
        if fails < 3:
            if q_level.lower() != "easy":
                print(pyfiglet.Figlet(font="small").renderText("Level Up!!!"))
            score, fails = quiz(score, fails, level_list_dict[q_level])
    return score


def get_user_choice():
    while True:
        choice = input("Enter your option number:").upper()
        if choice in ("A", "B", "C", "D"):
            return choice
        else:
            print("Enter your option number:Only A/B/C/D are accepted")


def quiz(score, fails, questions_list):
    i = 0
    # print("******* length of q list ", len(questions_list))
    try:
        for question in questions_list:
            i += 1  # increment question numbers.
            if fails >= 3:
                break

            print(f'\n{i}. {question["question"].strip().capitalize()}')
            print(f'\tA. {question["A"].strip().title()}\n\tB. {question["B"].strip().title()}\n\t'
                  f'C. {question["C"].strip().title()}\n\tD. {question["D"].strip().title()}')
            user_ans = get_user_choice()
            # print(user_ans, question["ans"])
            if user_ans == question["ans"]:
                score += int(question["points"])
                fails = 0
                print(f"✅️That's correct!! \n <<< Your score is {score} >>>")
            else:
                print("❌ Incorrect!")
                print(f"The answer is\033[91m \033[4m \033[1m{question[question['ans']].strip().title()} \033[0m")
                '''
                class color:
                   PURPLE = '\033[95m'
                   CYAN = '\033[96m'
                   DARKCYAN = '\033[36m'
                   BLUE = '\033[94m'
                   GREEN = '\033[92m'
                   YELLOW = '\033[93m'
                   RED = '\033[91m'
                   BOLD = '\033[1m'
                   UNDERLINE = '\033[4m'
                   END = '\033[0m'
                
                print(color.BOLD + 'Hello, World!' + color.END)
                '''
                fails += 1
    except EOFError:
        sys.exit()

    # print("ask next question")
    return score, fails


def get_user_name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            return name.title()
        else:
            print("Only alphabets accepted")


def main():
    name = get_user_name()
    final_score = begin_quiz("ScienceQuizData.csv")

    f = pyfiglet.Figlet(font="doom")
    print(f.renderText("Game   Ends"))
    print(f.renderText(f"{name}     your  score  is   {final_score}"))


if __name__ == "__main__":
    main()
