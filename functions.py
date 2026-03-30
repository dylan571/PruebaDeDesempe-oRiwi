def add_student(students, id, name, age, program, status):
    #Adds a new non existing student

    student_exist = look_students(students, id)

    if student_exist:
        return False #already exist
    
    students.append({
            'id' :id,
            'name':name.upper(),
            'age':age,
            'program':program,
            'status':status
        })
    
    return True

def look_students(students, id):
    for e in students:
            if e["id"] == id:
                return e
    return None

def update_student_list(students, id, new_id=None, new_age=None, new_program=None, new_status=None):
    student_update = look_students(students, id)
    if student_update:
        if new_age is not None:
            student_update["age"] = new_age
        if new_id is not None:
            student_update["id"] = new_id
        if new_program is not None:
            student_update["program"] = new_program
        if new_status is not None:
            student_update["status"] = new_status
        return True
    return False

def delete_student(students, id):
    student_update = look_students(students, id)
    if student_update:
        students.remove(student_update)
        return True
    return False