from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomRole(AbstractUser):
    ROLE_CHOICES = [
        (0, "Admin"),
        (1, "Staff"),
        (2, "Student"),
    ]

    role = models.IntegerField(default=0, choices=ROLE_CHOICES)
    age = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


department = [
    ("Computer Science", "computer science"),
    ("Information Technology", "information technology"),
    ("Electronics & Communication", "electronics & communication"),
    ("Mechanical Engineering", "mechanical engineering"),
    ("Civil Engineering", "civil engineering"),
    ("Electrical Engineering", "electrical engineering"),
    ("Arts & Science", "arts & science"),
]


class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=True)
    roll_no = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    department = models.CharField(
        choices=department, max_length=100, blank=True, null=True
    )
    photo = models.FileField(upload_to="students/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Staff(models.Model):
    name = models.CharField(max_length=200)
    staff_id = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    department = models.CharField(
        choices=department, max_length=100, blank=True, null=True
    )
    photo = models.ImageField(upload_to="staff/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
