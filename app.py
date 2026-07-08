students = []

def create_profile():
    """
    Create a new student profile

    """

    print("==== Create Student Profile ====")

    name = input("Enter Student name : ").strip()
    roll_no = input("Enter roll no : ").strip()
    branch = input("Enter the Branch : ").strip()
    year = input("Enter the Year : ").strip()
    career_goal = input("Enter the career goal : ").strip()


    # Basic validation
    if name == "":
        print("\nStudent name cannot be empty!!!")
        return

    # Create one student profile

    student = { 
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "year": year,
        "career_goal": career_goal
        }

    # Store inside the list

    students.append(student)

    print("\n✅ Student Profile Created Successfully!\n")


def view_profiles():
    """
    Display all student profiles.
    """

    print("\n===== Student Profiles =====")

    if len(students) == 0:
        print("No student profiles found.\n")
        return

    for index, student in enumerate(students, start=1):

        print(f"\nStudent {index}")

        print(f"Name          : {student['name']}")
        print(f"Roll Number   : {student['roll_no']}")
        print(f"Branch        : {student['branch']}")
        print(f"Year          : {student['year']}")
        print(f"Career Goal   : {student['career_goal']}")

    print()


def update_profile():
    """
    Update an existing student profile.
    """

    print("\n===== Update Student Profile =====")

    if len(students) == 0:
        print("No student profiles found.\n")
        return

    view_profiles()

    try:
        index = int(input("Enter the Student number to update : ")) - 1
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        return

    if index < 0 or index >= len(students):
        print("\nInvalid Student number!\n")
        return

    student = students[index]

    print("\nLeave field blank to keep the current value.\n")

    name = input(f"Enter Student name [{student['name']}] : ").strip()
    roll_no = input(f"Enter roll no [{student['roll_no']}] : ").strip()
    branch = input(f"Enter the Branch [{student['branch']}] : ").strip()
    year = input(f"Enter the Year [{student['year']}] : ").strip()
    career_goal = input(f"Enter the career goal [{student['career_goal']}] : ").strip()

    if name != "":
        student["name"] = name
    if roll_no != "":
        student["roll_no"] = roll_no
    if branch != "":
        student["branch"] = branch
    if year != "":
        student["year"] = year
    if career_goal != "":
        student["career_goal"] = career_goal

    print("\n✅ Student Profile Updated Successfully!\n")


def delete_profile():
    """
    Delete an existing student profile.
    """

    print("\n===== Delete Student Profile =====")

    if len(students) == 0:
        print("No student profiles found.\n")
        return

    view_profiles()

    try:
        index = int(input("Enter the Student number to delete : ")) - 1
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        return

    if index < 0 or index >= len(students):
        print("\nInvalid Student number!\n")
        return

    confirm = input(f"Are you sure you want to delete '{students[index]['name']}'? (y/n) : ").strip().lower()

    if confirm == "y":
        removed = students.pop(index)
        print(f"\n✅ Student Profile '{removed['name']}' Deleted Successfully!\n")
    else:
        print("\nDeletion cancelled.\n")


# ===========================
# Main Menu
# ===========================

while True: 
       print("1. Create Student Profile")
       print("2. View Student Profiles")
       print("3. Update Student Profile")
       print("4. Delete Student Profile")
       print("5. Exit")

       choice = input("\nEnter your choice : ")

       if choice == "1":

           create_profile()

       elif choice == "2":

           view_profiles()

       elif choice == "3":

           update_profile()

       elif choice == "4":

           delete_profile()

       elif choice == "5":

           print("\nThank you for using CareerPilot.")
           break

       else:
           print("\nInvalid Choice! Please try again.\n")

           