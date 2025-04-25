import tkinter as tk
from random import randint

# Define the board with snakes and ladders
board = {
    3: 22,  5: 8,   11: 26,  20: 29,  # Ladders
    27: 1,  21: 9,  17: 4,   19: 7    # Snakes
}

# Create the main application window
class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")

        self.players = ["Player 1", "Player 2"]
        self.positions = {"Player 1": 0, "Player 2": 0}
        self.current_player = 0

        self.create_widgets()

    def create_widgets(self):
        # Create the game board grid
        self.board_frame = tk.Frame(self.root)
        self.board_frame.grid(row=0, column=0, padx=20, pady=20)

        self.cells = {}
        for i in range(5):
            for j in range(6):
                num = i * 6 + j + 1
                cell_bg = "lightgreen" if num in board and board[num] > num else "lightcoral" if num in board else "white"
                cell_text = f"{num}\n\u2191 {board[num]}" if num in board and board[num] > num else f"{num}\n\u2193 {board[num]}" if num in board else str(num)
                cell = tk.Label(
                    self.board_frame, text=cell_text, width=6, height=3,
                    relief="solid", bg=cell_bg, font=("Arial", 10)
                )
                cell.grid(row=4 - i, column=j, padx=2, pady=2)
                self.cells[num] = cell

        # Create dice and player status
        self.status_frame = tk.Frame(self.root)
        self.status_frame.grid(row=0, column=1, padx=20, pady=20)

        self.dice_button = tk.Button(
            self.status_frame, text="Roll Dice", command=self.roll_dice
        )
        self.dice_button.pack(pady=10)

        self.dice_label = tk.Label(
            self.status_frame, text="Dice: -", font=("Arial", 14)
        )
        self.dice_label.pack(pady=10)

        self.info_label = tk.Label(
            self.status_frame, text=f"{self.players[self.current_player]}'s Turn",
            font=("Arial", 14), fg="blue"
        )
        self.info_label.pack(pady=10)

        self.position_labels = {
            player: tk.Label(self.status_frame, text=f"{player}: 0", font=("Arial", 12))
            for player in self.players
        }
        for label in self.position_labels.values():
            label.pack(pady=5)

    def roll_dice(self):
        dice = randint(1, 6)
        self.dice_label.config(text=f"Dice: {dice}")
        current = self.players[self.current_player]

        # Update player position
        self.positions[current] += dice
        if self.positions[current] > 30:
            self.positions[current] = 30

        # Check for snakes or ladders
        if self.positions[current] in board:
            self.positions[current] = board[self.positions[current]]

        # Update UI
        for num, cell in self.cells.items():
            cell.config(bg="lightgreen" if num in board and board[num] > num else "lightcoral" if num in board else "white")
        self.cells[self.positions[current]].config(bg="lightblue")

        self.position_labels[current].config(
            text=f"{current}: {self.positions[current]}"
        )

        # Check for winner
        if self.positions[current] == 30:
            self.info_label.config(text=f"{current} Wins!", fg="green")
            self.dice_button.config(state="disabled")
            return

        # Switch player
        self.current_player = (self.current_player + 1) % 2
        self.info_label.config(
            text=f"{self.players[self.current_player]}'s Turn"
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
