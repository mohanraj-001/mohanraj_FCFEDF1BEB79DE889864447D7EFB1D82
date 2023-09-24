def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Define a Student class for testing
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
student1 = Student("Alice", "001", 3.8)
student2 = Student("Bob", "002", 3.6)
student3 = Student("Charlie", "003", 3.9)
student4 = Student("David", "004", 3.7)

student_list = [student1, student2, student3, student4]

sorted_students = sort_students(student_list)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")