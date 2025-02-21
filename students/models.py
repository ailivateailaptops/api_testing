from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

def validate_grade(value):
    allowed_grades = ["A","A+","B","B+","C","C+","D","D+"]
    if value not in allowed_grades:
        raise ValidationError(f"Invalid grade. Allowed values: {allowed_grades}")

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(
        validators=[
            MinValueValidator(0, message="Age cannot be negative."),
            MaxValueValidator(120, message="Age cannot be more than 120.")
        ]
    )
    grade = models.CharField(
        max_length=2,
        validators=[validate_grade]  #  Custom validator
    )
    email = models.EmailField(unique=True)
