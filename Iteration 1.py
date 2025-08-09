import hashlib

# User class to store credentials and user data
class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.grade_tracker = GradeTracker()
        self.career_planner = CareerPlanner()
    
    def _hash_password(self, password):
        """Securely hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        """Verify password against stored hash"""
        return self.password_hash == self._hash_password(password)


class GradeTracker:
    def __init__(self):
        self.standards = []  # List of dictionaries

    def add_standard(self, title, level, credits, grade):
        self.standards.append({
            "title": title,
            "level": level,
            "credits": credits,
            "grade": grade.upper()
        })

    def total_credits(self, level=None):
        return sum(s["credits"] for s in self.standards if level is None or s["level"] == level)

    def credits_by_grade(self):
        result = {"E": 0, "M": 0, "A": 0, "N": 0}
        for s in self.standards:
            grade = s["grade"]
            if grade in result:
                result[grade] += s["credits"]
        return result

    def get_summary(self):
        return self.standards


class CareerPlanner:
    def __init__(self):
        self.interests = []
        self.careers = []

    def add_interest(self, interest):
        self.interests.append(interest.lower())

    def recommend_careers(self):
        self.careers = []  # Reset each time
        if "math" in self.interests or "physics" in self.interests:
            self.careers.append("Engineer")
        if "biology" in self.interests or "chemistry" in self.interests:
            self.careers.append("Doctor or Health Sciences")
        if "english" in self.interests or "history" in self.interests:
            self.careers.append("Lawyer or Writer")
        if not self.careers:
            self.careers.append("Explore more interests to unlock career suggestions")
        return self.careers


class Frost:
    def __init__(self):
        self.knowledge_base = {
            "engineering": "Engineering requires strong performance in Level 2 and 3 Maths and Physics. Aim for Merit or Excellence.",
            "medicine": "To study medicine in NZ, you'll need Biology, Chemistry, and high Excellence credits. UCAT is also required.",
            "law": "Law prefers students with strong reading, writing, and reasoning skills. Excellence in English helps.",
            "architecture": "Architecture combines creativity and science. Good grades in Graphics, Math, and Physics are recommended.",
            "computer science": "Strong performance in Math and Digital Tech is helpful. Aim for Merit or higher at Level 2 and 3.",
        }

    def answer(self, question):
        question = question.lower()
        for keyword in self.knowledge_base:
            if keyword in question:
                return self.knowledge_base[keyword]
        return "Frost doesn't know the answer to that yet. Try rephrasing your question!"


class GradusApp:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.frost = Frost()
    
    def register_user(self):
        print("\n--- Create New Account ---")
        username = input("Choose a username: ").strip()
        
        if username in self.users:
            print("Username already exists. Please choose another.")
            return False
        
        password = input("Create a password: ").strip()
        if len(password) < 4:
            print("Password must be at least 4 characters")
            return False
        
        self.users[username] = User(username, password)
        print("Account created successfully!")
        return True
    
    def login(self):
        print("\n--- Login ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        user = self.users.get(username)
        if not user or not user.verify_password(password):
            print("Invalid username or password")
            return False
        
        self.current_user = user
        print(f"Welcome back, {username}!")
        return True
    
    def logout(self):
        self.current_user = None
        print("You've been logged out.")
    
    def add_standard_ui(self):
        print("\n--- Add New Standard ---")
        title = input("Standard title: ").strip()
        
        try:
            level = int(input("Level (1-3): ").strip())
            if level < 1 or level > 3:
                raise ValueError
        except ValueError:
            print("Invalid level. Must be 1, 2, or 3.")
            return
        
        try:
            credits = int(input("Credits (1-24): ").strip())
            if credits < 1 or credits > 24:
                raise ValueError
        except ValueError:
            print("Invalid credits. Must be between 1-24.")
            return
        
        grade = input("Grade (E/M/A/N): ").strip().upper()
        if grade not in ['E', 'M', 'A', 'N']:
            print("Invalid grade. Must be E, M, A, or N.")
            return
        
        self.current_user.grade_tracker.add_standard(title, level, credits, grade)
        print("Standard added successfully!")
    
    def add_interest_ui(self):
        print("\n--- Add Interest ---")
        interest = input("Enter an interest/subject: ").strip()
        if interest:
            self.current_user.career_planner.add_interest(interest)
            print(f"Added '{interest}' to your interests!")
        else:
            print("Interest cannot be empty.")
    
    def view_summary(self):
        tracker = self.current_user.grade_tracker
        planner = self.current_user.career_planner
        
        print("\n--- Your Academic Summary ---")
        print(f"Total Credits: {tracker.total_credits()}")
        print(f"Level 1 Credits: {tracker.total_credits(level=1)}")
        print(f"Level 2 Credits: {tracker.total_credits(level=2)}")
        print(f"Level 3 Credits: {tracker.total_credits(level=3)}")
        print("\nCredit Breakdown by Grade:")
        for grade, credits in tracker.credits_by_grade().items():
            print(f"- {grade}: {credits} credits")
        
        print("\nYour Interests:")
        if planner.interests:
            for interest in planner.interests:
                print(f"- {interest.capitalize()}")
        else:
            print("No interests added yet")
        
        print("\nCareer Recommendations:")
        careers = planner.recommend_careers()
        for i, career in enumerate(careers, 1):
            print(f"{i}. {career}")
    
    def ask_frost(self):
        print("\n--- Ask Frost ---")
        print("Ask Frost about careers like Engineering, Medicine, Law, Architecture, or Computer Science")
        question = input("\nWhat career question do you have? ").strip()
        if question:
            print("\nFrost says:", self.frost.answer(question))
        else:
            print("Please enter a question.")
    
    def run(self):
        print("\n==============================================")
        print("    Welcome to Gradus - Your NCEA Career Companion")
        print("==============================================")
        print(" Frost is ready to help with career questions!\n")
        
        # Create a sample user for demonstration
        sample_user = User("sample", "student123")
        sample_user.grade_tracker.add_standard("Physics 2.4 - Mechanics", 2, 6, "E")
        sample_user.grade_tracker.add_standard("English 2.1 - Writing", 2, 4, "M")
        sample_user.grade_tracker.add_standard("Math 2.3 - Algebra", 2, 5, "A")
        sample_user.career_planner.add_interest("math")
        sample_user.career_planner.add_interest("physics")
        self.users["sample"] = sample_user
        
        # Main application loop
        while True:
            if not self.current_user:
                print("\nMAIN MENU:")
                print("1. Login")
                print("2. Register")
                print("3. Exit")
                choice = input("Choose an option: ").strip()
                
                if choice == '1':
                    self.login()
                elif choice == '2':
                    self.register_user()
                elif choice == '3':
                    print("\nThank you for using Gradus. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("\nMAIN MENU:")
                print("1. Add Standard")
                print("2. Add Interest")
                print("3. View Academic Summary")
                print("4. Ask Frost Career Questions")
                print("5. Logout")
                
                choice = input("Choose an option: ").strip()
                
                if choice == '1':
                    self.add_standard_ui()
                elif choice == '2':
                    self.add_interest_ui()
                elif choice == '3':
                    self.view_summary()
                elif choice == '4':
                    self.ask_frost()
                elif choice == '5':
                    self.logout()
                else:
                    print("Invalid choice. Please try again.")


# Run the app
if __name__ == "__main__":
    app = GradusApp()
    app.run()
