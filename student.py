import tkinter as tk
from tkinter import ttk

def assing_grade(score):
    if score>= 90:
        return 'A'
    elif score>= 80:
        return 'B'
    elif score>= 70:
        return 'C'
    elif score>= 60:
        return 'D'
    else:
        return 'F'

    def detemine_pass_fail(score):
        return "pass" if score >= 50 else "Fail"

    student = {
        "Alice": {"Math": 95, "Science": 88, "English": 92, "History": 85, "Art": 90},
        "Bob": {"Math": 82, "Science": 78, "English": 85, "History": 80, "Art": 75},
        "Charlie": {"Math": 73, "Science": 70, "English": 76, "History": 72, "Art": 75},
        "tej": {"Math": 61, "Science": 63, "English": 58, "History": 65, "Art": 60},
        "kalp": {"Math": 58, "Science": 55, "English": 52, "History": 60, "Art": 65},
        "sonu": {"Math": 45, "Science": 50, "English": 48, "History": 55, "Art": 50}
     }

    def show_results():
        root = tk.TK()
        root.title("Student Results")


        tree = ttk.Treeview(root , columns=("Student", "Average Score", "Greade", "Pass/Fail"), show="heading")
        tree.heading("Student", text="Student")
        tree.heading("Average Score", text="Average Score")
        tree.headin("Grade", text="Grade")
        tree.heading("Pass/ Fail", text="Pass/Fail")


    for student, subjects in students.items():
        total_score = sum(subjects.values())
        num_subjects = len(subjects)
        averang_score = totle_score / num_subjects
        grade = assign_grade(averang_score)
        pass_fail = determine_pass_fail(average_score)
        tree.insert("", tk.END, values=(student,"{average_score:.2f}", grade, pass_fail))

    tree.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

    show_results()

    
    
    
