allStudents = []


class Student:
    def __init__(self, name, roll_no, Branch, year, career_goal):
        self.name = name
        self.roll_no = roll_no
        self.Branch = Branch
        self.year = year
        self.career_goal = career_goal

        allStudents.append(self)
    
    def display_student(self):
        print("\n===== Student Profile =====")
        print(f"\nName          : {self.name}")
        print(f"Roll Number   : {self.roll_no}")
        print(f"Branch        : {self.Branch}")
        print(f"Year          : {self.year}")
        print(f"Career Goal   : {self.career_goal}") 
    
    def update_student(self, name=None, roll_no=None, Branch=None, year=None, career_goal=None):
        if name:
            self.name = name
        if roll_no:
            self.roll_no = roll_no
        if Branch:
            self.Branch = Branch
        if year:
            self.year = year
        if career_goal:
            self.career_goal = career_goal
    
    def delete_student(self):
        del self

class StudentProfileManager:
    def __init__(self):
        self.students = []

    def create_profile(self):
        print("\n===== Create Student Profile =====")

        name = input("Enter Student Name   : ").strip()
        roll_no = input("Enter Roll Number    : ").strip()
        Branch = input("Enter Branch         : ").strip()
        year = input("Enter Year           : ").strip()
        career_goal = input("Enter Career Goal   : ").strip()

        if name == "":
            print("\nStudent name cannot be empty!")
            return

        student = Student(name, roll_no, Branch, year, career_goal)
        self.students.append(student)

        print("\nStudent Profile Created Successfully!\n")

    def view_profiles(self):
        if not self.students:
            print("\nNo student profiles found.\n")
            return

        print("\n===== Student Profiles =====")
        for index, student in enumerate(self.students, start=1):
            print(f"\nStudent {index}")
            student.display_student()

    def update_profile(self):
        roll_no = input("Enter Roll Number of Student to Update: ").strip()
        for student in self.students:
            if student.roll_no == roll_no:
                print(f"\nUpdating Profile for Student with Roll Number: {roll_no}\n")
                name = input("Enter New Name (or press Enter to keep current): ").strip()
                Branch = input("Enter New Branch (or press Enter to keep current): ").strip()
                year = input("Enter New Year (or press Enter to keep current): ").strip()
                career_goal = input("Enter New Career Goal (or press Enter to keep current): ").strip()

                student.update_student(name=name or None, Branch=Branch or None, year=year or None, career_goal=career_goal or None)
                print(f"\nStudent Profile Updated Successfully for Roll Number: {roll_no}\n")
                return
        print(f"\nNo student found with Roll Number: {roll_no}\n")

    def delete_profile(self):
        roll_no = input("Enter Roll Number of Student to Delete: ").strip()
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"\nStudent Profile Deleted Successfully for Roll Number: {roll_no}\n")
                return
        print(f"\nNo student found with Roll Number: {roll_no}\n")

manager = StudentProfileManager()



class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def display_task(self):
        print("\n===== Task Details =====")
        print(f"Title       : {self.title}")
        print(f"Description : {self.description}")
        print(f"Due Date    : {self.due_date}")
        print(f"Status      : {'Completed' if self.completed else 'Pending'}")
    
    def mark_as_completed(self):
        self.completed = True
        print(f"\nTask '{self.title}' marked as completed.\n")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        print("\n===== Create New Task =====")
        title = input("Enter Task Title       : ").strip()
        description = input("Enter Task Description : ").strip()
        due_date = input("Enter Task Due Date    : ").strip()

        if title == "":
            print("\nTask title cannot be empty!")
            return

        task = Task(title, description, due_date)
        self.tasks.append(task)

        print("\nTask Created Successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.\n")
            return

        print("\n===== All Tasks =====")
        for index, task in enumerate(self.tasks, start=1):
            print(f"\nTask {index}")
            task.display_task()

    def mark_task_completed(self):
        title = input("Enter Title of Task to Mark as Completed: ").strip()
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                return
        print(f"\nNo task found with Title: {title}\n")

task_manager = TaskManager()




def StudentManager():
    
    while True:

        print("\n===== Student Profile Management System =====")
        print("1. Create Student Profile")
        print("2. View All Student Profiles")
        print("3. Update Student Profile")
        print("4. Delete Student Profile")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            manager.create_profile()
        elif choice == '2':
            manager.view_profiles()
        elif choice == '3':
            manager.update_profile()
        elif choice == '4':
            manager.delete_profile()
        elif choice == '5':
            print("\nThank you for using Career-Pilot\n")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.\n")






def Taskmanager():
            
        while True:
            print("\n===== Task Management System =====")
            print("1. Create New Task")
            print("2. View All Tasks")
            print("3. Mark Task as Completed")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                task_manager.create_task()
            elif choice == '2':
                task_manager.view_tasks()
            elif choice == '3':
                task_manager.mark_task_completed()
            elif choice == '4':
                print("\nThank you for using Career-Pilot\n")
                break
            else:
                print("\nInvalid choice! Please enter a number between 1 and 4.\n")





while True:

    print("===== Welcome to Career Pilot =====")

    print("Here are the options: ")
    print("1. Student Profile Management System")
    print("2. Task Management System")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == '1':
        
        StudentManager()

    elif choice == '2':
        
        Taskmanager()

    elif choice == '3':
        print("\nThank you for using Career-Pilot\n")
        break

    else:
        
        print("\nInvalid choice! Please enter a number between 1 and 3.\n")