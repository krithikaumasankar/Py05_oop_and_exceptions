#GRADE CALCULATOR
class student():
    def __init__(self):
        print("\n\tWELCOME TO GRADE CALCULATOR....!")
        self.name = input("Enter your name: ")
        self.marks = []
    def add_marks(self):
        for i in range(5):
            m = float(input("Enter marks: "))
            self.marks.append(m)
    def display(self):
        t = 0
        for i in self.marks:
            t += i
        avg = t / 5
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "R"
        else:
            grade = "F"
        print("Name:",self.name,"\nGrade:",grade,"\ntotal:",t,"\nAverage marks:",avg)
s = student()
s.add_marks()
s.display()
