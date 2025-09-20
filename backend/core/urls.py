from django.urls import path, include

urlpatterns = [
    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
    path("adminpanel/", include("adminpanel.urls")),
]
