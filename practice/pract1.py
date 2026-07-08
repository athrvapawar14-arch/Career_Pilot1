class Student: 
    print("==== Student Class ====")
    def __init__ (self, name = None , roll_no = None, branch = None):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.__marks = 99
        
        print(f"Student profile created successfully for {self.name}")


    def display_student(self):

        print("==== Student Profile ====")
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Branch : {self.branch}")
        


S1 = Student( "Athrva", 503 , "CSE-ITP")
S1.display_student()
print(S1._Student__marks)