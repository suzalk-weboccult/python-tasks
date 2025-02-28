"""
This module provides functionality to count students who achieved an A1 grade (greater than 90) and store student-grade mappings.

Functions:
- count_A1_grades(students, grades): Counts the number of students with A1 grades and stores student-grade data.
"""
def count_A1_grades(students, grades):
    """
    Count the number of students who achieved an A1 grade (greater than 90) and store student-grade mapping.

    Parameters:
    students (list): List of student names.
    grades (list): List of student grades corresponding to the students list.

    Returns:
    int: The count of students who have an A1 grade (greater than 90).
    """
    merit = {}  # Dictionary to store student names and their corresponding grades
    count = 0   # Counter for students with A1 grades

    # Iterate over the students list and assign grades to the merit dictionary
    for i in range(len(students)):
        merit[students[i]] = grades[i]

        # Check if the grade is greater than 90 (A1 grade)
        if grades[i] > 90:
            count += 1

    print(merit)  # Print the dictionary containing student-grade mapping
    return count


# Take user input for the number of students
num_students = int(input("Enter the number of students: "))

students = []  # List to store student names
grades = []    # List to store student grades

# Validate number of students input
while num_students <= 0:
    print("Number of students cannot be negative or zero")
    num_students = int(input("Enter the number of students: "))

# Input student names and grades
while num_students:
    student = input("Enter the name of a student: ")
    students.append(student)

    grade = int(input("Enter the grade (between 0-100) of a student: "))

    # Validate grade input
    while grade < 0 or grade > 100:
        print("Grade should be between 0-100")
        grade = int(input("Enter the grade (between 0-100) of a student: "))

    grades.append(grade)
    num_students -= 1

# Display the number of students with A1 grade
print("No. of students with A1 grade:", count_A1_grades(students, grades))
