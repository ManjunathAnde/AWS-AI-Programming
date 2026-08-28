#OOPS CONCEPTS using Classes and Inheritance
import math


class Student:
    """Base class representing a student with scores."""

    school = "AWS AI Academy"  # class attribute - shared by all

    def __init__(self, name, scores=None): #default arguement
        self.name = name                    # instance attribute
        self.scores = scores if scores else [] #if no scores, then empty list