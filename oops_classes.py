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

    