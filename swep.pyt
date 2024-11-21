import tkinter as tk
from tkinter import messagebox

# Sample database for courses, tests, and submissions
courses = {}
tests = {}
submissions = {}
# User database simulation (initially empty)
users = {}

class EducationPlatform:
    def _init_(self, root):
        self.root = root
        self.root.title("Education Platform")
        self.current_user = None
        self.current_role = None
        self.create_welcome_screen()
        self.root.configure(bg='blue')  # Set blue background for the root window

    def create_welcome_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="ONLINE LEARNING PLATFORM\nGROUP B PROJECT PRESENTED BY:\n\n\nOlayiwola Abdussomad Damilola\n\nAdeyemi Waliyulahi Adeyinka\n\nOladejo Fuhadudeen Ifeoluwa\n\nAzeez Samad Ajibola\n\nGaruba Abdulrasheed Ayobami\n\nAbidoye Naheem Oluwafemi\n\nJesurinu Ogooluwa Samuel\n\nAderonmu Mercy Tomisin\n\nOlarewaju Philip Ayomide\n\nAkanbi Victor Oluwaseyi", 
                  font=("Arial", 8), bg='blue', fg='white').pack(pady=50)
        tk.Button(self.root, text="Continue", command=self.role_selection_screen, bg='red', fg='white').pack(pady=20)

    def role_selection_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Select Your Role:", font=("Arial", 20), bg='blue', fg='white').pack(pady=20)
        tk.Button(self.root, text="Register as Student", command=self.register_student_screen, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Register as Teacher", command=self.register_teacher_screen, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Login as Student", command=self.login_student_screen, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Login as Teacher", command=self.login_teacher_screen, bg='green', fg='white').pack(pady=10)

    def register_student_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Student Registration", font=("Arial", 10), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Username:", bg='blue', fg='white').pack(pady=5)
        self.register_username = tk.Entry(self.root)
        self.register_username.pack(pady=5)
        tk.Label(self.root, text="Password:", bg='blue', fg='white').pack(pady=5)
        self.register_password = tk.Entry(self.root, show="*")
        self.register_password.pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register_student, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.role_selection_screen, bg='red', fg='white').pack(pady=5)

    def register_teacher_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Teacher Registration", font=("Arial", 10), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Username:", bg='blue', fg='white').pack(pady=5)
        self.register_username = tk.Entry(self.root)
        self.register_username.pack(pady=5)
        tk.Label(self.root, text="Password:", bg='blue', fg='white').pack(pady=5)
        self.register_password = tk.Entry(self.root, show="*")
        self.register_password.pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register_teacher, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.role_selection_screen, bg='red', fg='white').pack(pady=5)

    def login_student_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Student Login", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Username:", bg='blue', fg='white').pack(pady=5)
        self.login_username = tk.Entry(self.root)
        self.login_username.pack(pady=5)
        tk.Label(self.root, text="Password:", bg='blue', fg='white').pack(pady=5)
        self.login_password = tk.Entry(self.root, show="*")
        self.login_password.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login_student, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.role_selection_screen, bg='red', fg='white').pack(pady=5)

    def login_teacher_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Teacher Login", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Username:", bg='blue', fg='white').pack(pady=5)
        self.login_username = tk.Entry(self.root)
        self.login_username.pack(pady=5)
        tk.Label(self.root, text="Password:", bg='blue', fg='white').pack(pady=5)
        self.login_password = tk.Entry(self.root, show="*")
        self.login_password.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login_teacher, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.role_selection_screen, bg='red', fg='white').pack(pady=5)

    def register_student(self):
        username = self.register_username.get()
        password = self.register_password.get()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        if username in users:
            messagebox.showerror("Error", "Username already exists.")
        else:
            users[username] = {"password": password, "role": "student"}
            messagebox.showinfo("Success", "Registration successful!")
            self.role_selection_screen()

    def register_teacher(self):
        username = self.register_username.get()
        password = self.register_password.get()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        if username in users:
            messagebox.showerror("Error", "Username already exists.")
        else:
            users[username] = {"password": password, "role": "teacher"}
            messagebox.showinfo("Success", "Registration successful!")
            self.role_selection_screen()

    def login_student(self):
        username = self.login_username.get()
        password = self.login_password.get()
        if username in users and users[username]["password"] == password and users[username]["role"] == "student":
            self.current_user = username
            self.current_role = "student"
            self.student_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def login_teacher(self):
        username = self.login_username.get()
        password = self.login_password.get()
        if username in users and users[username]["password"] == password and users[username]["role"] == "teacher":
            self.current_user = username
            self.current_role = "teacher"
            self.teacher_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def student_dashboard(self):
        self.clear_frame()
        tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Arial", 10), bg='blue', fg='white').pack(pady=20)
        tk.Button(self.root, text="View Courses", command=self.view_courses, bg='red', fg='white').pack(pady=10)
        tk.Button(self.root, text="View Tests", command=self.view_and_submit_tests, bg='red', fg='white').pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout, bg='red', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.role_selection_screen, bg='red', fg='white').pack(pady=5)

    def teacher_dashboard(self):
        self.clear_frame()
        tk.Label(self.root, text=f"Welcome, {self.current_user} (Teacher)", font=("Arial", 10), bg='blue', fg='white').pack(pady=20)
        tk.Button(self.root, text="Add Course Content", command=self.add_course_content, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Add Test", command=self.add_test, bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout, bg='red', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.role_selection_screen, bg='red', fg='white').pack(pady=5)

    def add_course_content(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Course Content", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Course Name:", bg='blue', fg='white').pack(pady=5)
        course_name_entry = tk.Entry(self.root)
        course_name_entry.pack(pady=5)
        tk.Label(self.root, text="Content:", bg='blue', fg='white').pack(pady=5)
        content_entry = tk.Text(self.root, height=10, width=40)
        content_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=lambda: self.submit_course_content(course_name_entry.get(), content_entry.get("1.0", tk.END)), bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.teacher_dashboard, bg='red', fg='white').pack(pady=5)

    def submit_course_content(self, course_name, content):
        if course_name and content.strip():
            courses[course_name] = content.strip()
            messagebox.showinfo("Success", "Course content added successfully!")
            self.teacher_dashboard()
        else:
            messagebox.showerror("Error", "Course name and content cannot be empty.")

    def add_test(self):
        self.clear_frame()
        tk.Label(self.root, text="Add Test", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Test Name:", bg='blue', fg='white').pack(pady=5)
        test_name_entry = tk.Entry(self.root)
        test_name_entry.pack(pady=5)
        tk.Label(self.root, text="Test Content:", bg='blue', fg='white').pack(pady=5)
        content_entry = tk.Text(self.root, height=10, width=40)
        content_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=lambda: self.submit_test(test_name_entry.get(), content_entry.get("1.0", tk.END)), bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.teacher_dashboard, bg='red', fg='white').pack(pady=5)

    def submit_test(self, test_name, content):
        if test_name and content.strip():
            tests[test_name] = content.strip()
            messagebox.showinfo("Success", "Test added successfully!")
            self.teacher_dashboard()
        else:
            messagebox.showerror("Error", "Test name and content cannot be empty.")

    def view_courses(self):
        self.clear_frame()
        tk.Label(self.root, text="Available Courses", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        if courses:
            for course_name, content in courses.items():
                tk.Label(self.root, text=f"{course_name}:", font=("Arial", 14), bg='blue', fg='white').pack(pady=5)
                tk.Label(self.root, text=content, wraplength=400, bg='lightblue', fg='black').pack(pady=5)
        else:
            tk.Label(self.root, text="No courses available.", font=("Arial", 14), bg='blue', fg='white').pack(pady=5)
        tk.Button(self.root, text="Back", command=self.student_dashboard, bg='red', fg='white').pack(pady=10)

    def view_and_submit_tests(self):
        self.clear_frame()
        tk.Label(self.root, text="Available Tests", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        if tests:
            for test_name, content in tests.items():
                tk.Label(self.root, text=f"{test_name}:", font=("Arial", 14), bg='blue', fg='white').pack(pady=5)
                tk.Label(self.root, text=content, wraplength=400, bg='lightblue', fg='black').pack(pady=5)
                tk.Button(self.root, text="Submit Answer", command=lambda name=test_name: self.submit_test_answer(name), bg='green', fg='white').pack(pady=5)
        else:
            tk.Label(self.root, text="No tests available.", font=("Arial", 14), bg='blue', fg='white').pack(pady=5)
        tk.Button(self.root, text="Back", command=self.student_dashboard, bg='red', fg='white').pack(pady=10)

    def submit_test_answer(self, test_name):
        self.clear_frame()
        tk.Label(self.root, text=f"Submitting Answer for: {test_name}", font=("Arial", 16), bg='blue', fg='white').pack(pady=10)
        tk.Label(self.root, text="Your Answer:", bg='blue', fg='white').pack(pady=5)
        answer_entry = tk.Text(self.root, height=10, width=40)
        answer_entry.pack(pady=5)
        tk.Button(self.root, text="Submit", command=lambda: self.save_test_submission(test_name, answer_entry.get("1.0", tk.END)), bg='green', fg='white').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.view_and_submit_tests, bg='red', fg='white').pack(pady=5)

    def save_test_submission(self, test_name, answer):
        if answer.strip():
            if test_name not in submissions:
                submissions[test_name] = []
            submissions[test_name].append((self.current_user, answer.strip()))
            messagebox.showinfo("Success", "Answer submitted successfully!")
            self.view_and_submit_tests()
        else:
            messagebox.showerror("Error", "Answer cannot be empty.")

    def logout(self):
        self.current_user = None
        self.current_role = None
        self.role_selection_screen()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the GUI
root = tk.Tk()
app = EducationPlatform(root)
root.mainloop()
