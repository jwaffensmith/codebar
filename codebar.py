# PART I

# Super Class 

class Member:
    def __init__(self, full_name):
        self.name = full_name
    
    def introduce(self):
        return f"Hi, my name is {self.name}!"

# Student Sub Class
class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason
        self.full_name = full_name

    def state_reason(self):
        return self.reason

# Instructor Sub Class
class Instructor(Member):
    def __init__(self, full_name, bio) :
        super().__init__(full_name)
        self.bio = bio
        self.skills = []
        self.full_name = full_name
    
    def add_skill(self, add_skill):
        self.skills.append(add_skill)

#PART 2
#Workshop Sub Class

class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
        
    def add_participant(self, member):
        if type(member) == Student: 
            self.students.append(member)
        if type(member) == Instructor:
            self.instructors.append(member)
    
    def print_details(self):
        student_count = 0
        instructor_count = 0
        print(f"Workshop - {self.date} - {self.subject}")
        for student in self.students:
            student_count +=1
            print(f"Students \n {student_count}. {student.full_name} - {student.reason}")
        for instructor in self.instructors:
            instructor_count += 1
            print(f"Instructors \n {instructor_count}. {instructor.full_name} - {instructor.skills} \n {instructor.bio}")

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()

