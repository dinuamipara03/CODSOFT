from tkinter import *

# define question dictionary
question = {
    "Which is the largest island in the world?": [
        "Greenland",
        "Madagascar",
        "New Guinea",
        "Borneo",
    ],
    "What is the largest planet in our solar system?": [
        "Jupiter",
        "Saturn",
        "Mars",
        "Earth",
    ],
    "What is the chemical symbol for gold?": ["Go", "Au", "Ag", "Gd"],
    "Which gas is responsible for the greenhouse effect?": [
        "Carbon dioxide",
        "Methane",
        "Nitrous oxide",
        "Ozone",
    ],
}
# define answer list
ans = ["Greenland", "Jupiter", "Au", "Carbon dioxide"]

current_question = 0


def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()


def next_question():
    global current_question
    if current_question < len(question):
        # get key or question that need to be printed
        check_ans()
        user_ans.set("None")
        c_question = list(question.keys())[current_question]
        # clear frame to update its content
        clear_frame()
        # printing question
        Label(
            f1, text=f"Question : {c_question}", padx=15, font="calibre 12 normal"
        ).pack(anchor=NW)
        # printing options
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans, value=option, padx=28).pack(
                anchor=NW
            )
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Thanks for Participating", font="calibre 18 bold").pack()


def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != "None" and temp_ans == ans[current_question - 1]:
        user_score.set(user_score.get() + 1)


def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()


if __name__ == "__main__":
    root = Tk()
    # setup basic window
    root.title("QUIZ GAME")
    root.geometry("500x300")
    root.minsize(500, 300)

    # Centering the window
    window_width = 500
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry(
        f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}"
    )

    user_ans = StringVar()
    user_ans.set("None")
    user_score = IntVar()
    user_score.set(0)

    Label(
        root,
        text="Quiz Game",
        font="cambria 40 bold",
        relief=SUNKEN,
        padx=10,
        pady=9,
    ).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(
        root, text="Start Quiz", command=start_quiz, font="calibre 17"
    )
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next", command=next_question, font="calibre 17")

    root.mainloop()
