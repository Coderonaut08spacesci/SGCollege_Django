from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    search_query = request.GET.get("search", "")

    courses = Course.objects.filter(is_active=True)    
    if search_query:
        courses = courses.filter(
            name__icontains=search_query
        )

    return render(
        request,
        "core/course_list.html",
        {
            "courses": courses,
            "search_query": search_query,
        }
    )
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(
        request,
        "core/course_detail.html",
        {"course": course}
    )
    
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def fees(request):
    return render(request, "core/fees.html")


def principal_message(request):
    return render(request, "core/principal_message.html")


def syllabus(request):
    return render(request, "core/syllabus.html")