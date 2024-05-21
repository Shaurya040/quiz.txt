from tkinter import *

Round1_data = {
    "questions": {
        "Who developed Python Programming Language?": ['Wick van Rossum', 'Rasmus Lerdorf', 'Guido van Rossum', 'Niene Stom'],
        "Which type of Programming does Python support?": ['object-oriented programming', 'structured programming', 'functional programming', 'all of the mentioned'],
        "Is Python case sensitive when dealing with identifiers?": ['no', 'yes', 'machine dependent', 'none of the mentioned'],
    },
    "answers": ['Guido van Rossum', 'all of the mentioned', 'yes']
}

Round2_data = {
    "questions": {
        "Which of the following is used to define a block of code in Python language?": ['Indentation', 'Key', 'Brackets', 'All of the mentioned'],
        "What is the order of precedence in python?": ['Exponential, Parentheses, Multiplication, Division, Addition, Subtraction', 'Exponential, Parentheses, Division, Multiplication, Addition, Subtraction', 'Parentheses, Exponential, Multiplication, Division, Subtraction, Addition', 'Parentheses, Exponential, Multiplication, Division, Addition, Subtraction'],
        "What will be the output of the following Python code snippet if x=1? x<<2": ['4', '2', '1', '8'],
    },
    "answers": ['Indentation', 'Parentheses, Exponential, Multiplication, Division, Addition, Subtraction', '4']
}

Round3_data = {
    "questions": {
        "What will be the output of the following Python function?min(max(False,-3,-4), 2,7)": ['-4', '-3', '2', 'False'],
        "Which of the following statements is used to create an empty set in Python?": ['( )', '[ ]', '{ }', 'set()'],
        "Which function is called when the following Python program is executed?f = foo() , format(f)": ['trt', 'format()', 'str()', 'format_()'],
    },
    "answers": ['False', '{ }', 'str()']
}

Round4_data = {
    "questions": {
        "What is output of print(math.pow(3, 2))?": ['9.0', 'None', '9', 'None of the mentioned'],
        "Which one of the following is the use of function in python?": ['Functions dont provide better modularity for your application', 'you cant also create your own functions', 'Functions are reusable pieces of programs', 'All of the mentioned'],
        "What will be the output of the following Python Expression? round(4.576)": ['4', '4.6', '5', '4.5'],
    },
    "answers": ['9.0', 'All of the mentioned', '5']
}

rounds_data = [Round1_data, Round2_data, Round3_data, Round4_data]
current_round = 0
current_question = 0
user_score = 0
highest_score = 0

def start_quiz():
    global current_round, current_question, user_score, highest_score
    start_button.pack_forget()
    next_button.pack()
    current_round = 0
    current_question = 0
    user_score = 0
    highest_score = 0
    next_question()

def next_question():
    global current_round, current_question, user_score, highest_score
    if current_round < len(rounds_data):
        if current_question < len(rounds_data[current_round]["questions"]):
            check_ans()
            user_ans.set('')
            question = list(rounds_data[current_round]["questions"].keys())[current_question]
            clear_frame()
            Label(f1, text=f"Question : {question}", padx=15, font="calibre 12 normal").pack(anchor=NW)
            for option in rounds_data[current_round]["questions"][question]:
                Radiobutton(f1, text=option, variable=user_ans, value=option, padx=28).pack(anchor=NW)
            current_question += 1
        else:
            check_ans()
            current_question = 0
            if user_score == 3:
                Label(f1, text=f"Round {current_round + 1} Cleared! Score: {user_score}/3", font="calibre 12 bold").pack()
                current_round += 1
                user_score = 0
                if current_round < len(rounds_data):
                    next_question()
                else:
                    end_quiz()
            else:
                Label(f1, text=f"Round {current_round + 1} Failed. Score: {user_score}/3", font="calibre 12 bold").pack()
                next_button.pack_forget()
                start_button.pack()
    else:
        end_quiz()

def end_quiz():
    global highest_score
    next_button.pack_forget()
    clear_frame()
    output = f"Your Final Score is {highest_score} out of 12"
    if highest_score > 9:
        output += "\nCongratulations! You earned some points for scoring more than 9 out of 12."
    Label(f1, text=output, font="calibre 25 bold").pack()
    Label(f1, text="Thanks for Participating", font="calibre 18 bold").pack()

def check_ans():
    global user_score, highest_score
    if current_question > 0:
        temp_ans = user_ans.get()
        correct_ans = rounds_data[current_round]["answers"][current_question - 1]
        if temp_ans == correct_ans:
            user_score += 1
        highest_score = max(highest_score, user_score)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("GFG QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set('None')

    Label(root, text="Quiz App", font="calibre 40 bold", relief=SUNKEN, background="cyan", padx=10, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(root, text="Start Quiz", command=start_quiz, font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next Question", command=next_question, font="calibre 17 bold")
    next_button.pack()
    next_button.pack_forget()

    root.mainloop()
