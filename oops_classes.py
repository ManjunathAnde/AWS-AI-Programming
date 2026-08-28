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


