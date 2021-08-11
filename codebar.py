# PART I

# Super Class 
class Member:
    def __init__(self, full_name):
        self.name = full_name
    
    def introduce(self):
        print(f"Hi, my name is {self.name}!")

# Student Sub Class
class Student(Member):
    def __init__(self, full_name, attendance_reason):
        super().__init__(full_name)
        self.reason = attendance_reason

    def state_reason(self):
        print(self.reason)


jenna = Student("Jenna Waffensmith", "I love to code!")


# Instructor Sub Class
#class Instructor(Member):




#PART 2
#Workshops
