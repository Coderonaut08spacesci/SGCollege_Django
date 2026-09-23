from django.db import models

from core.models import Course


class Notice(models.Model):
    CATEGORY_CHOICES = [
        ("academic", "Academic"),
        ("examination", "Examination"),
        ("admission", "Admission"),
        ("event", "Event"),
        ("general", "General"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="general"
    )
    published_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=150)
    image = models.FileField(
        upload_to="event_images/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date", "time"]


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ["-submitted_at"]


class Admission(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="admissions"
    )

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)