from django.shortcuts import render, get_object_or_404
from .models import Course, Department, FeeStructure
from portal.models import Event


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
    events = Event.objects.all()[:3]

    return render(
        request,
        "core/home.html",
        {
            "events": events
        }
    )

def about(request):
    return render(request, "core/about.html")


def fees(request):
    fee_structures = FeeStructure.objects.all()

    return render(
        request,
        "core/fees.html",
        {
            "fee_structures": fee_structures
        }
    )


def principal_message(request):
    return render(request, "core/principal_message.html")


def syllabus(request):
    return render(request, "core/syllabus.html")

def photo_gallery(request):
    return render(request, "core/photo_gallery.html")