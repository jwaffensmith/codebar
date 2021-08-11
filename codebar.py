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

    def state_reason(self):
        return self.reason

# Instructor Sub Class
class Instructor(Member):
    def __init__(self, full_name, bio, skills:list):
        super().__init__(full_name)
        self.bio = bio
        self.skills = skills
    
    def add_skill(self, add_skill):
        self.add_skill = add_skill 
        self.skills.append(self.add_skill)


jenna = Student("Jenna Waffensmith", "I love to code!")
ali = Instructor("Ali Schaffer",  "I've been coding in Python for 5 years and want to share the love!", ["Python", "Javascript", "C++"])

#PART 2
#Workshops
