import tkinter as tk
from tkinter import messagebox

# Function to calculate the final grade
def calculate_grade():
    try:
        attendance = float(attendance_entry.get())
        unit_test = float(unit_test_entry.get())
        achievements = int(achievements_entry.get())
        mock_practical = float(mock_practical_entry.get())

        # Validating input ranges
        if not (0 <= attendance <= 100):
            raise ValueError("Attendance must be between 0 and 100.")
        if not (0 <= unit_test <= 50):
            raise ValueError("Unit Test score must be between 0 and 50.")
        if not (0 <= mock_practical <= 20):
            raise ValueError("Mock Practical score must be between 0 and 20.")
        
        # Calculate individual scores
        attendance_score = (attendance / 100) * 10  # 10% weightage
        unit_test_score = (unit_test / 50) * 50     # 50% weightage
        achievement_score = (achievements / 10) * 10  # 10% weightage
        mock_practical_score = (mock_practical / 20) * 30  # 30% weightage

        # Calculate final score
        final_score = round(attendance_score + unit_test_score + achievement_score + mock_practical_score, 2)

        # Display the grade and result
        result_label.config(
            text=f"Final Score: {final_score}/100\nGrade: {assign_grade(final_score)}",
            fg="green"
        )

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Function to assign a grade based on the final score
def assign_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

# GUI Setup
root = tk.Tk()
root.title("Automated Term Work Assessment")

# Labels and Entry Fields
tk.Label(root, text="Automated Term Work Assessment", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Attendance (%):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
attendance_entry = tk.Entry(root)
attendance_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Unit Test (/50):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
unit_test_entry = tk.Entry(root)
unit_test_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Achievements (/10):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
achievements_entry = tk.Entry(root)
achievements_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Mock Practical (/20):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
mock_practical_entry = tk.Entry(root)
mock_practical_entry.grid(row=4, column=1, padx=10, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade, bg="blue", fg="white")
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
