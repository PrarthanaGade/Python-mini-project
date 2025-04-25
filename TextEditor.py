import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox

class SmartTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Text Editor")
        self.root.geometry("900x600")
        self.root.config(bg="#1e1e2e")

        # Default settings
        self.current_font_family = "Arial"
        self.current_font_size = 14

        # Text Widget
        self.text_area = tk.Text(root, wrap="word", font=(self.current_font_family, self.current_font_size),
                                 fg="#ffffff", bg="#2b2b40", insertbackground="white", padx=10, pady=10)
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

        # Add Toolbar and Menus
        self.create_toolbar()
        self.create_menus()

        # Smart Suggestions
        self.suggestions = {
            "def": "def function_name():\n    pass",
            "class": "class ClassName:\n    def __init__(self):\n        pass",
            "if": "if condition:\n    pass",
            "for": "for i in range():\n    pass",
            "print": "print('')"
        }

        # Key Bindings
        self.text_area.bind("<Control-s>", self.save_file)
        self.text_area.bind("<Control-o>", self.open_file)
        self.text_area.bind("<Control-n>", self.new_file)
        self.text_area.bind("<space>", self.smart_suggestions)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg="#34344a")
        toolbar.pack(side="top", fill="x")

        # Font Selector
        font_label = tk.Label(toolbar, text="Font:", bg="#34344a", fg="#ffffff", padx=5)
        font_label.pack(side="left")

        self.font_box = tk.StringVar()
        font_menu = tk.OptionMenu(toolbar, self.font_box, "Arial", "Courier New", "Comic Sans MS", "Verdana",
                                  command=self.change_font)
        self.font_box.set(self.current_font_family)
        font_menu.pack(side="left", padx=5)

        # Font Size Selector
        size_label = tk.Label(toolbar, text="Size:", bg="#34344a", fg="#ffffff", padx=5)
        size_label.pack(side="left")

        self.size_box = tk.StringVar()
        size_menu = tk.OptionMenu(toolbar, self.size_box, *[str(size) for size in range(8, 40)], command=self.change_font_size)
        self.size_box.set(str(self.current_font_size))
        size_menu.pack(side="left", padx=5)

        # Change Text Color
        color_button = tk.Button(toolbar, text="Text Color", bg="#555577", fg="#ffffff", command=self.change_text_color)
        color_button.pack(side="left", padx=10)

        # Change Background Color
        bg_button = tk.Button(toolbar, text="Background Color", bg="#555577", fg="#ffffff", command=self.change_bg_color)
        bg_button.pack(side="left", padx=10)

    def create_menus(self):
        menu_bar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def new_file(self, event=None):
        self.text_area.delete(1.0, tk.END)
        self.root.title("Untitled - Smart Text Editor")

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.text_area.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"{file_path} - Smart Text Editor")

    def save_file(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{file_path} - Smart Text Editor")
            messagebox.showinfo("Save", "File saved successfully!")

    def change_font(self, new_font):
        self.current_font_family = new_font
        self.text_area.config(font=(self.current_font_family, self.current_font_size))

    def change_font_size(self, new_size):
        self.current_font_size = int(new_size)
        self.text_area.config(font=(self.current_font_family, self.current_font_size))

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(bg=color)

    def smart_suggestions(self, event):
        words = self.text_area.get("1.0", tk.END).split()
        if words and words[-1] in self.suggestions:
            self.text_area.insert(tk.END, "\n" + self.suggestions[words[-1]])

    def show_about(self):
        messagebox.showinfo("About", "Smart Text Editor v2.0\nEnhanced with Fonts, Colors, and Improved GUI!")

# Run the editor
if __name__ == "__main__":
    root = tk.Tk()
    editor = SmartTextEditor(root)
    root.mainloop()
