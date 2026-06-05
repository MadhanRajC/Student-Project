from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views import View


def user_login(request):
    context = {"error": ""}

    if request.user.is_authenticated:
        return redirect("/home/")

    if request.method == "POST":

        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("/home/")
        else:
            context = {"error": "Invalid Username or Password"}
            return render(request, "profile/login.html", context)

    return render(request, "profile/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("/")


def signup_user(request):

    if request.method == "POST":
        # 1. Create User
        user = CustomRole.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],  # create_user() hashes the password
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            age=request.POST["age"],
            role=request.POST["role"],
        )

        # 2. Create Profile
        Profile.objects.create(user=user)
        return redirect("/")

    return render(request, "profile/signup.html")


@login_required
def home(request):
    students = Student.objects.all()
    staffs = Staff.objects.all()
    return render(
        request,
        "home.html",
        {"student": students, "staff": staffs, "user": request.user},
    )


class Student_list(LoginRequiredMixin, View):
    login_url = "/"

    def get(self, request):
        students = Student.objects.all()
        return render(request, "student_list.html", {"student": students})


@login_required
def student_create(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        roll_no = request.POST.get("roll_no")
        email = request.POST.get("email")
        dept = request.POST.get("department")
        photo = request.FILES.get("photo")

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            roll_no=roll_no,
            email=email,
            department=dept,
            photo=photo,
        )
        student.save()
        return redirect("student-list")

    return render(request, "student_form.html")


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student_detail.html", {"student": student})


class Student_update(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(
            request,
            "student_form.html",
            {"student": student},
        )

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.roll_no = request.POST.get("roll_no")
        student.email = request.POST.get("email")
        student.department = request.POST.get("department")

        # file upload
        if request.FILES.get("photo"):
            student.photo = request.FILES["photo"]

        student.save()
        return redirect("student-list")


class Student_delete(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect("student-list")


# Staff
def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, "staff_list.html", {"staffs": staffs})


def staff_create(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        staff_id = request.POST.get("staff_id")
        email = request.POST.get("email")
        dept = request.POST.get("department")
        photo = request.FILES.get("photo")

        Staff_data = Staff.objects.create(
            name=fullname,
            staff_id=staff_id,
            email=email,
            department=dept,
            photo=photo,
        )
        Staff_data.save()
        return redirect("staff-list")

    return render(
        request,
        "staff_form.html",
    )


def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, "staff_detail.html", {"staff": staff})


def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)

    if request.method == "POST":
        staff.name = request.POST.get("fullname")
        staff.staff_id = request.POST.get("staff_id")
        staff.email = request.POST.get("email")
        staff.department = request.POST.get("department")

        # file upload
        if request.FILES.get("photo"):
            staff.photo = request.FILES["photo"]

        staff.save()
        return redirect("staff-list")

    return render(
        request,
        "staff_form.html",
        {"staff": staff},
    )


def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    staff.delete()
    return redirect("staff-list")
