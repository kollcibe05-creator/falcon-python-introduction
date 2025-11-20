import json

data_file ="db.json"

def read_student_data():
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
            if isinstance (data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    
def save_student_data(students):
    try:
         with open(data_file, "w") as file:
             json.dump(students, file, indent=4)
    except FileExistsError:
        return "File aleady exist"
    
def add_new_student():
    students = read_student_data()
    student_id = input("Student id: ")
    student_name = input("Student name: ")
    student_email = input("Student email: ")
    students.append({"Student id": student_id, "Student name": student_name, "Student email":student_email})
    save_student_data(students)
    print("Student saved successfully.")
    
def view_student_data():
    print("Student data")
    
def main():
    while True:
        print("\n Student management system")
        print("1. Add new student ")
        print("2. View students")
        print("3. Edit Student")
        print("4. Delete student")
        print("5. Exit")
        
        option  =input("Select an option:")
        if option == "1":
            add_new_student()
        elif option == "2":
            print("Method yet to be created!")
        elif option == "3":
            print("Method yet to be created!")
        elif option == "4":
            print("Method yet to be created!")
        elif option == "5":
            print("Exiting...")
        else:
            print("Option invalid")
            
if __name__ == "__main__":
    main()