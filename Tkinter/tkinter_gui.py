
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("450x450")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=15)

# Main frame
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=5)

# Student Name
tk.Label(frame, text="Student Name:", bg="lightblue",
         font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=8, sticky="w")
name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=0, column=1, pady=8)

# Roll Number
tk.Label(frame, text="Roll Number:", bg="lightblue",
         font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=8, sticky="w")
roll_entry = tk.Entry(frame, width=25)
roll_entry.grid(row=1, column=1, pady=8)

# Email
tk.Label(frame, text="Email:", bg="lightblue",
         font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=8, sticky="w")
email_entry = tk.Entry(frame, width=25)
email_entry.grid(row=2, column=1, pady=8)

# Gender
tk.Label(frame, text="Gender:", bg="lightblue",
         font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=8, sticky="w")

gender = tk.StringVar(value="Male")

tk.Radiobutton(frame, text="Male", variable=gender,
               value="Male", bg="lightblue").grid(row=3, column=1, sticky="w")

tk.Radiobutton(frame, text="Female", variable=gender,
               value="Female", bg="lightblue").grid(row=3, column=1, padx=80, sticky="w")

# Course
tk.Label(frame, text="Course:", bg="lightblue",
         font=("Arial", 11)).grid(row=4, column=0, padx=10, pady=8, sticky="w")

course = ttk.Combobox(
    frame,
    values=["Computer Science", "Information Technology",
            "Mechanical", "Civil"],
    width=22,
    state="readonly"
)
course.grid(row=4, column=1, pady=8)
course.set("Computer Science")

# Register function
def register():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not roll or not email:
        messagebox.showwarning("Warning", "Please fill all fields!")
    else:
        messagebox.showinfo(
            "Registration Successful",
            f"Name: {name}\nRoll No: {roll}\n"
            f"Email: {email}\nGender: {gender.get()}\n"
            f"Course: {course.get()}"
        )

# Clear function
def clear():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender.set("Male")
    course.set("Computer Science")

# Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Register", command=register,
          bg="green", fg="white", width=12).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Clear", command=clear,
          bg="orange", width=12).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Exit", command=root.destroy,
          bg="red", fg="white", width=12).grid(row=0, column=2, padx=10)

# Run application
root.mainloop()
