#OOPS CONCEPTS using Classes and Inheritance
import math


class Student:
    """Base class representing a student with scores."""

    school = "AWS AI Academy"  # class attribute - shared by all

    def __init__(self, name, scores=None): #default arguement
        self.name = name                    # instance attribute
        self.scores = scores if scores else [] #if no scores, then empty list
    def add_score(self, score):
        """Add a single score."""
        self.scores.append(score)

    def average(self):
        """Calculate average score."""
        if not self.scores: #If no scores exist, return 0
            return 0
        return sum(self.scores) / len(self.scores)

    def highest(self):
        """Return the highest score."""
        if not self.scores:
            return 0
        return max(self.scores)

    def passed(self, cutoff=50): #default cutoff is 50
        """Check if average is above cutoff."""
        return self.average() >= cutoff

    def __str__(self):
        """What print(object) shows."""
        status = "PASS" if self.passed() else "FAIL"
        return f"{self.name} | Avg: {self.average():.1f} | {status}"

    def __add__(self, other):
        """Combine two students' scores into a new group."""
        combined_name = f"{self.name} & {other.name}"
        combined_scores = self.scores + other.scores
        return Student(combined_name, combined_scores)

class AIStudent(Student):
    """Child class - inherits from Student, adds AI-specific details."""

    def __init__(self, name, scores=None, language="Python"):
        super().__init__(name, scores)       # reuse parent arguements using super()
        self.language = language             # new attribute of child class


    def read_scores_from_file(self, filename):
        """Load scores from a text file (one number per line)."""
        try:
            with open(filename, "r") as f:
                self.scores = [float(line.strip()) for line in f if line.strip()]
        except FileNotFoundError:
            print(f"File '{filename}' not found")

    def summary(self):
        """Full stats summary."""
        return (
            f"Student   : {self.name}\n"
            f"Language  : {self.language}\n"
            f"Scores    : {self.scores}\n"
            f"Average   : {self.average():.2f}\n"
            f"Highest   : {self.highest()}\n"
            f"Std Dev   : {self.stdev():.2f}\n"
            f"Status    : {'PASS' if self.passed() else 'FAIL'}"
        )

    def __str__(self):
        """Override parent's __str__ to include language."""
        status = "PASS" if self.passed() else "FAIL"
        return f"{self.name} ({self.language}) | Avg: {self.average():.1f} | {status}"


# --- Main block: only runs when executed directly ---

if __name__ == "__main__":

    # Basic Student
    s1 = Student("Mj", [85, 90, 78])
    s2 = Student("Roy", [92, 88, 95])
    print("--- Base Students ---")
    print(s1)
    print(s2)

    # __add__ in action
    combined = s1 + s2
    print(f"\nCombined: {combined}")

    # AI Student (child class)
    print("\n--- AI Student ---")
    ai = AIStudent("Manju", [88, 72, 95, 63, 81], "Python")
    print(ai.summary())

    # Class attribute
    print(f"\nSchool: {ai.school}")

    # Adding a score dynamically
    ai.add_score(91)
    print(f"\nAfter adding 91: Avg = {ai.average():.1f}")   
