# gradus.py

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
        self.grade_tracker = GradeTracker()
        self.career_planner = CareerPlanner()
        self.frost = Frost()

    def run(self):
        print("Welcome to Gradus — Your NCEA Career Companion")
        print(" Frost is ready to help with career questions!\n")

        # Simulate test input
        self.grade_tracker.add_standard("Physics 2.4 - Mechanics", 2, 6, "E")
        self.grade_tracker.add_standard("English 2.1 - Writing", 2, 4, "M")
        self.grade_tracker.add_standard("Math 2.3 - Algebra", 2, 5, "A")

        self.career_planner.add_interest("math")
        self.career_planner.add_interest("physics")

        print("Total Credits:", self.grade_tracker.total_credits())
        print("Credits by Grade:", self.grade_tracker.credits_by_grade())

        print("\n Career Suggestions Based on Interests:", self.career_planner.recommend_careers())
        print("\n Frost says:", self.frost.answer("What do I need to study engineering?"))


# Run the app (for testing)
if __name__ == "__main__":
    app = GradusApp()
    app.run()
