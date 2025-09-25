class Student:
    # Initialize a Student object with basic info, grades, and courses
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else []

    # String representation for easy display
    def __str__(self):
        return (f"Student ID: {self.student_id}\n"
                f"Student Name: {self.student_name}\n"
                f"Email: {self.email}\n"
                f"Grades: {self.grades}\n"
                f"Courses: {self.courses}")

class StudentRecords:
    def __init__(self):
        self.students = []  # List to store all student objects
    
    # Add a new student to the records
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
        return "Student added successfully."
    
    # Update student details by ID
    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.student_id == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                return "Student updated successfully."
        return "Student not found."
    
    # Calculate GPA based on letter grades
    def calculate_gpa(self, student_id):
        grade_scale = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        
        for student in self.students:
            if student.student_id == student_id:
                if not student.grades:
                    return "No grades available."
                total_points = 0
                count = 0
                for grade in student.grades.values():
                    gpa = grade_scale.get(grade.upper())
                    if gpa is not None:
                        total_points += gpa
                        count += 1
                if count == 0:
                    return "No valid grades to calculate GPA."
                return round(total_points / count, 2)
        return "Student not found."
    
    # Search for students by name (case-insensitive)
    def search_by_name(self, student_name):
        results = [str(student) for student in self.students if student_name.lower() in student.student_name.lower()]
        return results if results else "No student found."

    # Remove a student from the records by ID
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return "Student deleted successfully."
        return "Student not found."
    
    # Enroll a student in a new course if not already enrolled
    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.student_id == student_id:
                if course not in student.courses:
                    student.courses.append(course)
                    return "Course enrolled successfully."
                else:
                    return "Student already enrolled in this course."
        return "Student not found." 
    
    # Search for a student by ID
    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return str(student)
        return "Student not found." 


records = StudentRecords()

# Adding a new student: Louis Emmanuel Navarro
print("===== Adding Student: Louis Emmanuel Navarro =====")
print(records.add_student("24-53262", "Louis Emmanuel Navarro", "louisnavarro@gmail.com", {"Math": "A", "Science": "B"}, ["Math", "Science"]))
print()
     
# Adding a new student: Neil Patrick Mamiit
print("===== Adding Student: Neil Patrick Mamiit =====")
print(records.add_student("24-32333", "Neil Patrick Mamiit", "neilpatrickmamiit@example.com", {"Math": "A", "Science": "A", "English": "A"}, ["Math", "Science", "English"]))
print()

# Calculating GPA for Neil Patrick Mamiit
print("===== Calculating GPA for Neil Patrick Mamiit =====")
print(records.calculate_gpa("24-32333"))
print()

# Searching for student by name
print("===== Searching for Student by Name 'Neil' =====")
print(records.search_by_name("Neil"))
print()

# Deleting a student
print("===== Deleting Student: Louis Navarro =====")
print(records.delete_student("24-53262"))
print()

# Verifying deletion
print("===== Searching for the deleted student =====")
print(records.search_student("24-53262"))
print()
