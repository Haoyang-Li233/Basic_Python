class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# from Student import student

s1 = student("Edward", "ECE", 100)
s2 = student("Edw", "CEC", 10)

print(s1.on_honor_roll())
