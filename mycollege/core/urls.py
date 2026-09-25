from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("about/", views.about, name="about"),

    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),

    path("fees/", views.fees, name="fees"),

    path(
        "principal-message/",
        views.principal_message,
        name="principal_message"
    ),

    path("syllabus/", views.syllabus, name="syllabus"),
]