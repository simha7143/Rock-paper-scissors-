import random
import tkinter as tk
from tkinter import messagebox

# Initialize scores and round count
user_score = 0
computer_score = 0
rounds_to_win = 3

# Emoji-based choices
choices = {
    'rock': '🪨 Rock',
    'paper': '📄 Paper',
    'scissors': '✂️ Scissors'
}

def get_computer_choice():
    return random.choice(list(choices.keys()))

def determine_winner(user, computer):
    global user_score, computer_score

    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        user_score += 1
        return "You win this round!"
    else:
        computer_score += 1
        return "Computer wins this round!"

def update_scoreboard():
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

def check_game_over():
    if user_score == rounds_to_win:
        messagebox.showinfo("Game Over", "🎉 Congratulations! You won the game!")
        disable_buttons()
    elif computer_score == rounds_to_win:
        messagebox.showinfo("Game Over", "💻 Computer won the game. Try again!")
        disable_buttons()

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(
        text=f"Your Choice: {choices[user_choice]}\n"
             f"Computer's Choice: {choices[computer_choice]}\n"
             f"Result: {result}"
    )
    update_scoreboard()
    check_game_over()

def disable_buttons():
    for button in [rock_btn, paper_btn, scissors_btn]:
        button.config(state=tk.DISABLED)

def enable_buttons():
    for button in [rock_btn, paper_btn, scissors_btn]:
        button.config(state=tk.NORMAL)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scoreboard()
    result_label.config(text="")
    enable_buttons()

# GUI Setup
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x450")
window.resizable(False, False)

title_label = tk.Label(window, text="Rock-Paper-Scissors", font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

score_label = tk.Label(window, text="Score: You 0 - 0 Computer", font=('Arial', 12))
score_label.pack(pady=5)

result_label = tk.Label(window, text="", font=('Arial', 11), justify="center")
result_label.pack(pady=10)

# Buttons for choices
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=12, font=('Arial', 12),
                     command=lambda: play('rock'))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, font=('Arial', 12),
                      command=lambda: play('paper'))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, font=('Arial', 12),
                         command=lambda: play('scissors'))
scissors_btn.grid(row=0, column=2, padx=5)

# Restart Button
reset_button = tk.Button(window, text="🔁 Restart Game", font=('Arial', 11),
                         bg="lightblue", command=reset_game)
reset_button.pack(pady=20)

# Run the application
window.mainloop()
