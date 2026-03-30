import functions as functions

students = []

def request_int(message):
    """Request a valid value"""
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Can't be negative")
                continue
            return value
        except ValueError:
            print("❌ Enter a valid number")


while True:

    print("\nMENU\n")
    print("1. Register a student.")
    print("2. Check student list.")
    print("3. Search student.")
    print("4. Update student information.")
    print("5. Delete student.")
    print("0. Salir")

    try:
        op = int(input("Option: \n"))
    except ValueError:
        print("❌ Wrong enter")
        continue

    if op == 1:
        #Add new student
        id = request_int("Enter students ID =")
        name = input("Enter students name =") 
        age = request_int("Enter students age =")
        program = input("Enter students program =")
        status = input("Enter students status =")
            
        if functions.add_student(students, id, name, age, program, status):
            print("✅\nStudent registered with success")
        else:
            print("❌ ID already exist")

    if op == 2:
        #Check student list
        print("\nSTUDENT LIST\n")
        if not students:
            print("No student registered")
        for e in students:
            print(f"ID: {e['id']} - Name: {e['name']} - Age: {e['age']} - Program: {e['program']} - Status: {e['status']}")

    elif op == 3:
        #Seach student by name
        id = request_int("Search by ID: ")
        result = functions.look_students(students, id)
        if result:
            print("✅ Found:", result)
        else:
            print("❌ Not found")
        
    elif op == 4:
        #Update student list

        id = request_int("Enter the student's id to update: ")
        new_id = request_int("Enter new id (leave in blank not to update): ")
        new_age = request_int("Enter new age (leave in blank not to update): ")
        new_program = input("Enter new program (leave in blank not to update): ")
        new_status = input("Enter new status (leave in blank not to update): ")
        if functions.update_student_list(students, id, new_id, new_age, new_program, new_status):
            print("✅ Updated")
        else:
            print("❌ Student not found, can't update...")

    elif op == 5:
        #Delete a student from student list
        id = request_int("Enter student's ID to delete: ")
        if functions.delete_student(students, id):
            print("✅ Deleted")
        else:
            print("❌ Not found")

    elif op == 0:
        print("👋 Leaving...")
        break





    

    