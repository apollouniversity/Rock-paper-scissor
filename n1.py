import tkinter as tk
import random

class Congrats:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=700, bg="#263238", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.create_text_with_shadow("Congratulations.. You Win", 400, 300)
        
        self.colors = ["#fce18a", "#ff726d", "#b48def", "#f4306d"]
        self.create_congrats()

    def create_text_with_shadow(self, text, x, y):
        text_shadow_effects = [
            (5, 5, "#eb452b"), (10, 10, "#efa032"), (15, 15, "#46b59b"), 
            (20, 20, "#017e7f"), (25, 25, "#052939"), (30, 30, "#c11a2b")
        ]
        for dx, dy, color in text_shadow_effects:
            self.canvas.create_text(x + dx, y + dy, text=text, font=("Helvetica", 50, "bold"), fill=color)
        self.canvas.create_text(x, y, text=text, font=("Helvetica", 50, "bold"), fill="#fcedd8")
    
    def create_congrats(self):
        for _ in range(50):
            size = random.randint(5, 15)
            x = random.randint(0, 800)
            y = -size
            color = random.choice(self.colors)
            speed = random.uniform(2, 6)
            self.animate_congrats(x, y, size, color, speed)

    def animate_congrats(self, x, y, size, color, speed):
        if y < 700:
            congrats = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
            self.root.after(int(50 * speed), lambda: self.canvas.delete(congrats))
            self.root.after(50, lambda: self.animate_congrats(x, y + speed * 3, size, color, speed))

class SadTheme:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=700, bg="#ff0000", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.create_message("Sorry, You Lost the Game\nAll the Best for the Next Game", 400, 200)
        self.sad_symbols = ["😢", "😭", "☹️", "😞"]
        self.create_sad_symbols()
        
    def create_message(self, text, x, y):
        self.canvas.create_text(x, y, text=text, font=("Courier", 40, "bold"), fill="white", justify="center")

    def create_sad_symbols(self):
        for _ in range(50):
            size = random.randint(30, 60)
            x = random.randint(0, 800)
            y = random.randint(75, 600)
            symbol = random.choice(self.sad_symbols)
            self.animate_symbol(x, y, symbol, size)

    def animate_symbol(self, x, y, symbol, size):
        symbol_id = self.canvas.create_text(x, y, text=symbol, font=("Courier", size, "bold"), fill="white")
        self.canvas.after(5000, self.canvas.delete, symbol_id)
class TieTheme:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=700, bg="#d3d3d3", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.create_message("It's a Tie!", 400, 200)
        self.create_handshake()
    
    def create_message(self, text, x, y):
        self.canvas.create_text(x, y, text=text, font=("Helvetica", 50, "bold"), fill="#000000", justify="center")

    def create_handshake(self):
        self.canvas.create_text(400, 400, text="🤝", font=("Helvetica", 100), fill="#000000")

def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    
    button_rock.config(bg="gray")
    button_paper.config(bg="gray")
    button_scissors.config(bg="gray")
    
    if user_choice == "Rock":
        button_rock.config(bg="green")
    elif user_choice == "Paper":
        button_paper.config(bg="green")
    elif user_choice == "Scissors":
        button_scissors.config(bg="green")
    
    label_result.config(text="Waiting...", fg="blue", font=("Arial", 20, "bold"))
    root.after(1000, reveal_result, user_choice)  

def reveal_result(user_choice):
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    
    label_result.config(text=f"You: {emoji_map[user_choice]}  VS  Computer: {emoji_map[comp_choice]}\n{result}", 
                        fg="red", font=("Arial", 20, "bold"))
    
    update_stats(result)

    if result == "You win!":
        show_congrats()
    elif result == "Computer wins!":
        show_sad_theme()
    else:
        show_tie_theme()

def update_stats(result):
    global user_wins, computer_wins, ties
    if result == "You win!":
        user_wins += 1
    elif result == "Computer wins!":
        computer_wins += 1
    else:
        ties += 1

    label_user_wins.config(text=f"Your Wins: {user_wins}", font=("Arial", 16, "bold"))
    label_computer_wins.config(text=f"Computer Wins: {computer_wins}", font=("Arial", 16, "bold"))
    label_ties.config(text=f"Ties: {ties}", font=("Arial", 16, "bold"))
    root.update_idletasks()

def reset_stats():
    global user_wins, computer_wins, ties
    user_wins = computer_wins = ties = 0
    
    label_user_wins.config(text=f"Your Wins: {user_wins}", font=("Arial", 16, "bold"))
    label_computer_wins.config(text=f"Computer Wins: {computer_wins}", font=("Arial", 16, "bold"))
    label_ties.config(text=f"Ties: {ties}", font=("Arial", 16, "bold"))

def show_congrats():
    congrats_window = tk.Toplevel(root)
    congrats_window.geometry("800x700")
    congrats_window.configure(bg="#263238")
    Congrats(congrats_window)

def show_sad_theme():
    sad_window = tk.Toplevel(root)
    sad_window.geometry("800x700")
    sad_window.configure(bg="#ff0000")
    SadTheme(sad_window)

def show_tie_theme():
    tie_window = tk.Toplevel(root)
    tie_window.geometry("800x700")
    tie_window.configure(bg="#d3d3d3")
    TieTheme(tie_window)

user_wins = 0
computer_wins = 0
ties = 0

emoji_map = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x600")
root.config(bg="#f7f7f7")

label_user_wins = tk.Label(root, text=f"Your Wins: {user_wins}", font=("Arial", 22, "bold"), bg="#f7f7f7")
label_user_wins.pack(pady=10)

label_computer_wins = tk.Label(root, text=f"Computer Wins: {computer_wins}", font=("Arial", 22, "bold"), bg="#f7f7f7")
label_computer_wins.pack(pady=10)

label_ties = tk.Label(root, text=f"Ties: {ties}", font=("Arial", 22, "bold"), bg="#f7f7f7")
label_ties.pack(pady=10)

label_result = tk.Label(root, text="Choose your move to start the game!", font=("Arial", 20, "bold"), bg="#f7f7f7")
label_result.pack(pady=20)

button_rock = tk.Button(root, text="✊ROCK", font=("Arial", 50, "bold"), width=10, command=lambda: play_game("Rock"), bg="#ffcc00", activebackground="#ff9900")
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="✋PAPER", font=("Arial", 50, "bold"), width=10, command=lambda: play_game("Paper"), bg="#ffcc00", activebackground="#ff9900")
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="✌️SCISSOR", font=("Arial", 50, "bold"), width=10, command=lambda: play_game("Scissors"), bg="#ffcc00", activebackground="#ff9900")
button_scissors.pack(pady=5)

button_reset = tk.Button(root, text="Reset Stats", font=("Arial", 16, "bold"), command=reset_stats, bg="#ff6666", activebackground="#ff4d4d")
button_reset.pack(pady=20)

root.mainloop()
