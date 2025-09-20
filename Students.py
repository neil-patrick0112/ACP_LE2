class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grade is not None else {}
        self.courses = courses if courses is not None else []

    def __str__(self):
        return (f"Student ID: {self.student_id} \n"
                f"Student Name {self.student_name} \n"
                f"Email: {self.email} \n"
                f"Grades: {self.grades} \n"
                f"Courses: {self.courses}")
    
class StudentRecords:
    def __init__(self):
        self.students = []
    
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully."
