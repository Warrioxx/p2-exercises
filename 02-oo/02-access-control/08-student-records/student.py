class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

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
        letterGrade = self.calculate_letter_grade(score);
        self.__courses[course_name] = letterGrade

    def get_courses(self):
        return self.__courses