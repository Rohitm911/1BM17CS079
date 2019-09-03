class student:
    def __init__(self):
        self.id = 0
        self.age = 0
        self.marks = 0
    def validate_marks(self):
        if self.marks >= 0 and self.marks <= 100:
            return True
        else:
            return False
    def validate_age(self):
        if self.age > 20:
            return True
        else:
            print("age is lesser than 21")
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.marks >= 65:
                return True
            else:
                print("Marks are lesser than 65")
                return False
        else:
            return False
    def set_details(self, usn, age, marks):
        self.id = usn
        self.age = age
        self.marks = marks
    
    def get_details(self):
        if self.check_qualification():
            print("You got selected!")
            print("student id : ",self.id)
            print("student age : ",self.age)
            print("student marks : ",self.marks)
        else:
            print("Sorry, not qualified for selection!")

stud = student()
usn = input("Enter your student id : ")
age = int(input("Enter your age : "))
marks = int(input("Enter marks : "))
stud.set_details(usn,age,marks)
stud.get_details()
        
         
