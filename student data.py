def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def determine_pass_fail(score):
    return "Pass" if score >= 50 else "Fail"

# Example usage
students = {
    "Alice": {"Math": 95, "Science": 88, "English": 92, "History": 85, "Art": 90},
    "Bob": {"Math": 82, "Science": 78, "English": 85, "History": 80, "Art": 75},
    "Charlie": {"Math": 73, "Science": 70, "English": 76, "History": 72, "Art": 75},
    "David": {"Math": 61, "Science": 63, "English": 58, "History": 65, "Art": 60},
    "Eve": {"Math": 58, "Science": 55, "English": 52, "History": 60, "Art": 65},
    "Frank": {"Math": 45, "Science": 50, "English": 48, "History": 55, "Art": 50}
}

for student, subjects in students.items():
    total_score = sum(subjects.values())
    num_subjects = len(subjects)
    average_score = total_score / num_subjects
    grade = assign_grade(average_score)
    pass_fail = determine_pass_fail(average_score)
    print(f"{student} has an average score of {average_score:.2f}, a grade of {grade}, and has {pass_fail}ed.")
