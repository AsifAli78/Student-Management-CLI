# Dictionary to store student data (ID as key, name as value)
student_data = {}

def add_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_data[student_id] = student_name
    print(f"Student {student_name} with ID {student_id} added successfully.")

def remove_student():
    student_id = input("Enter student ID to remove: ")
    if student_id in student_data:
        student_name = student_data.pop(student_id)
        print(f"Student {student_name} with ID {student_id} removed successfully.")
    else:
        print("Student not found.")

def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in student_data:
        print(f"Student ID: {student_id}, Name: {student_data[student_id]}")
    else:
        print("Student not found.")

def edit_student():
    student_id = input("Enter student ID to edit: ")
    if student_id in student_data:
        new_name = input("Enter the new name for the student: ")
        student_data[student_id] = new_name
        print(f"Student {student_id} updated with the new name: {new_name}")
    else:
        print("Student not found.")

def list_students():
    print("\nList of Students:")
    for student_id, student_name in student_data.items():
        print(f"Student ID: {student_id}, Name: {student_name}")

def total_students():
    print(f"Total number of students: {len(student_data)}")

while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. List Students")
    print("6. Total Students")
    print("7. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        edit_student()
    elif choice == "5":
        list_students()
    elif choice == "6":
        total_students()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
