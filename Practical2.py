def _avg_marks(marks):
    total = 0
    count = 0
    for mark in marks:
        if mark != -1:  # Exclude absent students
            total += mark
            count += 1
    if count > 0:
        avg = total / count
    else:
        avg = 0
    print("Average marks of the class is:", avg)


def _highest_marks(marks):
    max_marks = -1
    for mark in marks:
        if mark > max_marks and mark != -1:  # Exclude absent students
            max_marks = mark
    print("Highest marks in the class is:", max_marks)


def _lowest_marks(marks):
    min_marks = 100
    for mark in marks:
        if mark < min_marks and mark != -1:  # Exclude absent students
            min_marks = mark
    print("Lowest marks in the class is:", min_marks)


def _absent_students(marks):
    absent_count = 0
    for mark in marks:
        if mark == -1:
            absent_count += 1
    print("Number of absent students is:", absent_count)


def _frequency_of_students(marks):
    frequency = {}
    for mark in marks:
        if mark != -1:  # Exclude absent students
            if mark in frequency:
                frequency[mark] += 1
            else:
                frequency[mark] = 1
    print("Frequency of marks:", frequency)


# Main program
marks = []
num = int(input("Enter the number of students: "))
for i in range(num):
    while True:
        try:
            mark = int(input(f"Enter the marks of student {i + 1} (-1 for absent): "))
            if mark >= -1:
                marks.append(mark)
                break
            else:
                print("Please enter a valid mark (-1 or greater).")
        except ValueError:
            print("Invalid input! Please enter an integer.")

while True:
    print("\n1. Average marks of the class")
    print("2. Highest marks in the class")
    print("3. Lowest marks in the class")
    print("4. Number of absent students")
    print("5. Frequency of students")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            _avg_marks(marks)
        elif choice == 2:
            _highest_marks(marks)
        elif choice == 3:
            _lowest_marks(marks)
        elif choice == 4:
            _absent_students(marks)
        elif choice == 5:
            _frequency_of_students(marks)
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
