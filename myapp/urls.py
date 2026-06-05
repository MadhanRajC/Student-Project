from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login),
    path("logout/", views.user_logout),
    path("signup/", views.signup_user),
    path("home/", views.home, name="home"),
    # Students
    path("students/", views.Student_list.as_view(), name="student-list"),
    path("students/create/", views.student_create, name="student-create"),
    path("students/<int:pk>/", views.student_detail, name="student-detail"),
    path(
        "students/edit/<int:pk>/", views.Student_update.as_view(), name="student-update"
    ),
    path(
        "students/delete/<int:pk>/",
        views.Student_delete.as_view(),
        name="student-delete",
    ),
    # # Staff
    path("staff/", views.staff_list, name="staff-list"),
    path("staff/create/", views.staff_create, name="staff-create"),
    path("staff/<int:pk>/", views.staff_detail, name="staff-detail"),
    path("staff/edit/<int:pk>/", views.staff_update, name="staff-update"),
    path("staff/delete/<int:pk>/", views.staff_delete, name="staff-delete"),
]
