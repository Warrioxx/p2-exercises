class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def calculate_letter_grade(self, score):
        if score < 60:
            return "F"
        elif score < 70:
            return "D"
        elif score < 80:
            return "C"
        elif score < 90:
            return "B"
        else:
            return "A"


    def add_course(self, course_name, score):
        pass

    def get_courses(self):
        pass