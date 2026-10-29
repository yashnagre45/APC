import os
import re
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(APP_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "students.csv")
SUBJECTS = ["Python", "Mathematics", "Computer Networks"]
ATTENDANCE_LIMIT = 75


def prepare_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        columns = ["roll_no", "name", "email"] + SUBJECTS + ["attended", "conducted"]
        pd.DataFrame(columns=columns).to_csv(DATA_FILE, index=False)


def load_students():
    prepare_files()
    try:
        df = pd.read_csv(DATA_FILE).fillna("")
        return df.to_dict("records")
    except (OSError, pd.errors.EmptyDataError, pd.errors.ParserError):
        return []


def save_students(students):
    columns = ["roll_no", "name", "email"] + SUBJECTS + ["attended", "conducted"]
    try:
        pd.DataFrame(students, columns=columns).to_csv(DATA_FILE, index=False)
        return True
    except (OSError, ValueError) as error:
        messagebox.showerror("Save Error", f"Could not save student records:\n{error}")
        return False


def valid_email(email):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None


def numeric_value(value, label, minimum, maximum):
    try:
        number = float(value)
    except ValueError:
        raise ValueError(f"{label} must be a number.")
    if not minimum <= number <= maximum:
        raise ValueError(f"{label} must be between {minimum} and {maximum}.")
    return number


def get_percentage(student):
    marks = [float(student.get(subject, 0) or 0) for subject in SUBJECTS]
    return sum(marks) / len(SUBJECTS)


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"


def get_attendance(student):
    conducted = float(student.get("conducted", 0) or 0)
    attended = float(student.get("attended", 0) or 0)
    return (attended / conducted * 100) if conducted > 0 else 0


class ScholarTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ScholarTrack | Student Performance & Attendance")
        self.root.geometry("1120x700")
        self.root.minsize(960, 600)
        self.root.configure(bg="#f4f7fb")
        self.students = load_students()
        self.build_ui()
        self.refresh_table()

    def build_ui(self):
        header = tk.Frame(self.root, bg="#172554", padx=24, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="ScholarTrack", font=("Segoe UI", 25, "bold"),
                 bg="#172554", fg="white").pack(anchor="w")
        tk.Label(header, text="Student Performance & Attendance Management System",
                 font=("Segoe UI", 11), bg="#172554", fg="#dbeafe").pack(anchor="w")

        cards = tk.Frame(self.root, bg="#f4f7fb", padx=18, pady=14)
        cards.pack(fill="x")
        self.total_card = self.make_card(cards, "TOTAL STUDENTS", "0")
        self.average_card = self.make_card(cards, "CLASS AVERAGE", "0%")
        self.topper_card = self.make_card(cards, "TOP PERFORMER", "—")
        self.low_att_card = self.make_card(cards, "LOW ATTENDANCE", "0")
        for card in (self.total_card, self.average_card, self.topper_card, self.low_att_card):
            card.pack(side="left", fill="x", expand=True, padx=5)

        form = tk.LabelFrame(self.root, text="Student Details", bg="white",
                             fg="#172554", padx=12, pady=10, font=("Segoe UI", 10, "bold"))
        form.pack(fill="x", padx=22, pady=5)

        self.entries = {}
        fields = [
            ("Roll No", "roll_no"), ("Student Name", "name"), ("Email", "email"),
            ("Python /100", "Python"), ("Maths /100", "Mathematics"),
            ("Networks /100", "Computer Networks"), ("Attended Lectures", "attended"),
            ("Total Lectures", "conducted")
        ]
        for index, (label, key) in enumerate(fields):
            row, col = divmod(index, 4)
            tk.Label(form, text=label, bg="white", fg="#334155").grid(
                row=row*2, column=col, sticky="w", padx=7, pady=(2, 0))
            entry = ttk.Entry(form, width=23)
            entry.grid(row=row*2+1, column=col, sticky="ew", padx=7, pady=(2, 8))
            self.entries[key] = entry
            form.columnconfigure(col, weight=1)

        actions = tk.Frame(form, bg="white")
        actions.grid(row=4, column=0, columnspan=4, sticky="w", padx=7, pady=2)
        tk.Button(actions, text="Add Student", command=self.add_student,
                  bg="#2563eb", fg="white", relief="flat", padx=14, pady=7).pack(side="left", padx=(0, 8))
        tk.Button(actions, text="Update Selected", command=self.update_student,
                  bg="#0f766e", fg="white", relief="flat", padx=14, pady=7).pack(side="left", padx=8)
        tk.Button(actions, text="Delete Selected", command=self.delete_student,
                  bg="#dc2626", fg="white", relief="flat", padx=14, pady=7).pack(side="left", padx=8)
        tk.Button(actions, text="Clear Form", command=self.clear_form,
                  bg="#64748b", fg="white", relief="flat", padx=14, pady=7).pack(side="left", padx=8)

        search_frame = tk.Frame(self.root, bg="#f4f7fb", padx=22, pady=8)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="Search by roll number or name:",
                 bg="#f4f7fb", fg="#334155").pack(side="left")
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=8)
        self.search_entry.bind("<KeyRelease>", lambda event: self.refresh_table())
        tk.Button(search_frame, text="Class Report", command=self.show_report,
                  bg="#172554", fg="white", relief="flat", padx=14, pady=5).pack(side="right")

        table_frame = tk.Frame(self.root, bg="#f4f7fb", padx=22, pady=5)
        table_frame.pack(fill="both", expand=True)
        columns = ("roll_no", "name", "percentage", "grade", "attendance", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        headings = {
            "roll_no": "Roll No", "name": "Student Name", "percentage": "Average %",
            "grade": "Grade", "attendance": "Attendance %", "status": "Attendance Status"
        }
        widths = {"roll_no": 100, "name": 250, "percentage": 120, "grade": 90, "attendance": 140, "status": 180}
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="center")
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        footer = tk.Label(self.root, text="Select a student row to edit or delete • Records are saved in data/students.csv",
                          bg="#e2e8f0", fg="#334155", padx=10, pady=8)
        footer.pack(fill="x")

    def make_card(self, parent, title, value):
        frame = tk.Frame(parent, bg="white", padx=14, pady=12, highlightbackground="#dbe3ef", highlightthickness=1)
        tk.Label(frame, text=title, font=("Segoe UI", 9, "bold"),
                 bg="white", fg="#64748b").pack(anchor="w")
        value_label = tk.Label(frame, text=value, font=("Segoe UI", 18, "bold"),
                               bg="white", fg="#172554")
        value_label.pack(anchor="w", pady=(5, 0))
        frame.value_label = value_label
        return frame

    def read_form(self):
        data = {key: entry.get().strip() for key, entry in self.entries.items()}
        if not data["roll_no"] or not data["name"]:
            raise ValueError("Roll number and student name are required.")
        if not valid_email(data["email"]):
            raise ValueError("Enter a valid email address.")
        for subject in SUBJECTS:
            data[subject] = numeric_value(data[subject], subject + " marks", 0, 100)
        data["attended"] = numeric_value(data["attended"], "Attended lectures", 0, 100000)
        data["conducted"] = numeric_value(data["conducted"], "Total lectures", 1, 100000)
        if data["attended"] > data["conducted"]:
            raise ValueError("Attended lectures cannot exceed total lectures.")
        return data

    def add_student(self):
        try:
            data = self.read_form()
            if any(str(student["roll_no"]).lower() == data["roll_no"].lower() for student in self.students):
                raise ValueError("That roll number already exists.")
            self.students.append(data)
            if save_students(self.students):
                self.refresh_table()
                self.clear_form()
                messagebox.showinfo("Success", "Student added successfully.")
        except ValueError as error:
            messagebox.showwarning("Check Details", str(error))

    def update_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Student", "Select a student row first.")
            return
        try:
            data = self.read_form()
            old_roll = self.tree.item(selected[0], "values")[0]
            if data["roll_no"] != old_roll and any(
                str(s["roll_no"]).lower() == data["roll_no"].lower() for s in self.students
            ):
                raise ValueError("That roll number already exists.")
            for index, student in enumerate(self.students):
                if str(student["roll_no"]) == str(old_roll):
                    self.students[index] = data
                    break
            if save_students(self.students):
                self.refresh_table()
                self.clear_form()
                messagebox.showinfo("Updated", "Student record updated.")
        except ValueError as error:
            messagebox.showwarning("Check Details", str(error))

    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Student", "Select a student row first.")
            return
        roll = self.tree.item(selected[0], "values")[0]
        if messagebox.askyesno("Confirm Delete", f"Delete student {roll}?"):
            self.students = [s for s in self.students if str(s["roll_no"]) != str(roll)]
            if save_students(self.students):
                self.refresh_table()
                self.clear_form()

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.category_focus()

    def category_focus(self):
        self.entries["roll_no"].focus_set()

    def on_select(self, event=None):
        selected = self.tree.selection()
        if not selected:
            return
        roll = self.tree.item(selected[0], "values")[0]
        for student in self.students:
            if str(student["roll_no"]) == str(roll):
                for key, entry in self.entries.items():
                    entry.delete(0, tk.END)
                    entry.insert(0, str(student.get(key, "")))
                break

    def refresh_table(self):
        query = self.search_entry.get().strip().lower() if hasattr(self, "search_entry") else ""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for student in self.students:
            if query and query not in str(student["roll_no"]).lower() and query not in str(student["name"]).lower():
                continue
            percentage = get_percentage(student)
            attendance = get_attendance(student)
            status = "Low Attendance" if attendance < ATTENDANCE_LIMIT else "Eligible"
            self.tree.insert("", tk.END, values=(
                student["roll_no"], student["name"], f"{percentage:.1f}",
                get_grade(percentage), f"{attendance:.1f}%", status
            ))
        count = len(self.students)
        average = sum(get_percentage(s) for s in self.students) / count if count else 0
        topper = max(self.students, key=get_percentage)["name"] if count else "—"
        low_count = sum(get_attendance(s) < ATTENDANCE_LIMIT for s in self.students)
        self.total_card.value_label.config(text=str(count))
        self.average_card.value_label.config(text=f"{average:.1f}%")
        self.topper_card.value_label.config(text=topper[:16])
        self.low_att_card.value_label.config(text=str(low_count))

    def show_report(self):
        if not self.students:
            messagebox.showinfo("Class Report", "Add students to generate a report.")
            return
        count = len(self.students)
        average = sum(get_percentage(s) for s in self.students) / count
        topper = max(self.students, key=get_percentage)
        low = [s for s in self.students if get_attendance(s) < ATTENDANCE_LIMIT]
        lines = [
            f"Total students: {count}",
            f"Class average: {average:.2f}%",
            f"Top performer: {topper['name']} ({get_percentage(topper):.2f}%)",
            f"Students below {ATTENDANCE_LIMIT}% attendance: {len(low)}",
            "",
            "Attendance alerts:"
        ]
        lines.extend([f"- {s['name']}: {get_attendance(s):.1f}%" for s in low] or ["- None"])
        messagebox.showinfo("ScholarTrack Class Report", "\n".join(lines))


if __name__ == "__main__":
    prepare_files()
    root = tk.Tk()
    app = ScholarTrackApp(root)
    root.mainloop()
