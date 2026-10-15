# STUDENT PERFORMANCE ANALYZER

def validate_score(students):
    valid_students = []
    for student in students:
        if 0 < student["score"] <= 100:
            valid_students.append(student)

    return valid_students

def calculate_grade(valid_students):

    for student in valid_students:
        if 90 <= student["score"] <= 100:
            student["grade"] = "A"
            student["status"] = "PASS"
            
        elif 80 <= student["score"] <= 89:
            student["grade"] = "B"
            student["status"] = "PASS"
            
        elif 70 <= student["score"] <= 79:
            student["grade"] = "C"
            student["status"] = "PASS"
            
        elif 60 <= student["score"] <= 69:
            student["grade"] = "D"
            student["status"] = "PASS"
            
        elif student["score"] < 60:
            student["grade"] = "F"
            if student["score"] < 50:
                student["status"] = "FAIL"
            else:
                student["status"] = "PASS"

    return valid_students
        
def highest_lowest(valid_students):
    highest = 0
    lowest = float("inf")
    for student in valid_students:
        if student["score"] < lowest:
            lowest = student["score"]
            
        elif student["score"] > highest:
            highest = student["score"]

    return [highest, lowest]

def passed_failed(valid_students):
    passed = 0
    failed = 0
    for student in valid_students:
        if student["status"] == "FAIL":
            failed += 1
            continue
        passed += 1

    return [passed, failed]

def report(students):
    valid_students = validate_score(students)
    graded = calculate_grade(valid_students)
    [highest, lowest] = highest_lowest(graded)
    [passed,failed] = passed_failed(graded)

    return f"CLASS REPORT\nTotal number of students: {len(students)}\nNumber of students with valid grades: {len(valid_students)}\nHighest Score: {highest}, Lowest Score: {lowest}\nNumber of Students Passed: {passed}\nNumber of students Failed: {failed}"


students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

print(report(students))