import tkinter as tk
from tkinter import ttk

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
    "tej": {"Math": 61, "Science": 63, "English": 58, "History": 65, "Art": 60},
    "kalp": {"Math": 58, "Science": 55, "English": 52, "History": 60, "Art": 65},
    "sonu": {"Math": 45, "Science": 50, "English": 48, "History": 55, "Art": 50}
}

def show_results():
    # Create the main window
    root = tk.Tk()
    root.title("Student Results")

    # Configure the style for the treeview to include grid lines
    style = ttk.Style()
    style.configure("Treeview", rowheight=25, bordercolor='black', borderwidth=1, relief='solid')
    style.configure("Treeview.Heading", font=('Calibri', 12, 'bold'))
    style.map("Treeview", background=[('selected', 'blue')], foreground=[('selected', 'white')])

    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
    style.configure("Treeview", borderwidth=1, relief="solid", background="white", foreground="black", fieldbackground="white")
    style.map("Treeview", background=[('selected', '#347083')], foreground=[('selected', 'white')])

    # Create a treeview to display the results
    tree = ttk.Treeview(root, columns=("Student", "Average Score", "Grade", "Pass/Fail"), show="headings")
    tree.heading("Student", text="Student")
    tree.heading("Average Score", text="Average Score")
    tree.heading("Grade", text="Grade")
    tree.heading("Pass/Fail", text="Pass/Fail")

    for student, subjects in students.items():
        total_score = sum(subjects.values())
        num_subjects = len(subjects)
        average_score = total_score / num_subjects
        grade = assign_grade(average_score)
        pass_fail = determine_pass_fail(average_score)
        tree.insert("", tk.END, values=(student, f"{average_score:.2f}", grade, pass_fail))

    tree.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

# Show results in a table
show_results()
