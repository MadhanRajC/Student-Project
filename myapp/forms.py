from django import forms
from .models import Student, Staff, Course
from django.contrib.auth.models import User
from .models import Profile


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "roll_no",
            "email",
            "department",
            "courses",
            "photo",
        ]
        widgets = {
            "courses": forms.CheckboxSelectMultiple,
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "staff_id", "email", "department", "photo"]


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["department", "title", "code", "description"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]
