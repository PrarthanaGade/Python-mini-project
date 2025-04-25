#Function to accept the names of students who play a specific sport
def _accept_args(student_list, sports):
    num_students = int(input(f"Enter the number of students who play {sports}: "))
    student_list = []
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1} who play {sports}: ")
        student_list.append(name)
    return student_list

#Function to display the list of students who play a specific sport
def _display_args(student_list, sports):
    if not student_list:
        print(f"No students currently registered for {sports}")
    else:
        print(f"\nStudents who play {sports}:")
        for i, student in enumerate(student_list, 1):
            print(f"{i}. {student}")

#Function to search for a student in the list
def _search_args(student_list, name):
    if name in student_list:
        print(f"{name} is present in the list")
    else:
        print(f"{name} is not present in the list")

#function to find the intersection of two lists
def _intersection_args(sports_list1, sports_list2):
    intersection = []
    for student in sports_list1:
        if student in sports_list2:
            intersection.append(student)
    return intersection

#function to find the union of two sports
def _union_args(sports_list1, sports_list2, union_list):
    for student in sports_list1:
        if student not in sports_list2:
            union_list.append(student)
    for student in sports_list2:
        if student not in sports_list1:
            union_list.append(student)
    return union_list

def _main():
    cricket_list = []
    badmiton_list = []
    football_list = []
    
    while True:
        print("\nMenu")
        print("1. Accept the names of students")
        print("2. Display the list of students")
        print("3. Search for a student")
        print("4. Students who play both cricket and badminton")
        print("5. Students who play either cricket or badminton but not both")
        print("6. Students who play neither cricket nor football")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        result = []

        if choice == 7:
            print("Thank you for using the program!")
            break
        elif choice == 1:
            print("\nWhich sport's students do you want to add?")
            print("1. Cricket")
            print("2. Badminton")
            print("3. Football")
            sport_choice = int(input("Enter your choice (1-3): "))
            
            if sport_choice == 1:
                cricket_list = _accept_args(cricket_list, "cricket")
                print("Cricket list updated successfully!")
            elif sport_choice == 2:
                badmiton_list = _accept_args(badmiton_list, "badminton")
                print("Badminton list updated successfully!")
            elif sport_choice == 3:
                football_list = _accept_args(football_list, "football")
                print("Football list updated successfully!")
            else:
                print("Invalid choice!")
        elif choice == 2:
            print("\nWhich sport's list do you want to display?")
            print("1. Cricket")
            print("2. Badminton")
            print("3. Football")
            print("4. All Sports")
            sport_choice = int(input("Enter your choice (1-4): "))
            
            if sport_choice == 1:
                _display_args(cricket_list, "cricket")
            elif sport_choice == 2:
                _display_args(badmiton_list, "badminton")
            elif sport_choice == 3:
                _display_args(football_list, "football")
            elif sport_choice == 4:
                _display_args(cricket_list, "cricket")
                _display_args(badmiton_list, "badminton")
                _display_args(football_list, "football")
            else:
                print("Invalid choice!")
        elif choice == 3:
            name = input("Enter the name of the student: ")
            print(f"Searching for {name} in all lists:")
            _search_args(cricket_list, name)
            _search_args(badmiton_list, name)
            _search_args(football_list, name)
        elif choice == 4:
            result = _intersection_args(cricket_list, badmiton_list)
            _display_args(result, "both cricket and badminton")
        elif choice == 5:
            # Students who play either cricket or badminton but not both
            cricket_only = [student for student in cricket_list if student not in badmiton_list]
            badminton_only = [student for student in badmiton_list if student not in cricket_list]
            result = cricket_only + badminton_only
            _display_args(result, "either cricket or badminton but not both")
        elif choice == 6:
            # Students who play neither cricket nor football
            all_students = set(cricket_list + badmiton_list + football_list)
            cricket_football = set(cricket_list + football_list)
            result = list(all_students - cricket_football)
            _display_args(result, "neither cricket nor football")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    _main()
            
            
            