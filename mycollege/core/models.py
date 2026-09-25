from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    hod = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        ordering = ["name"]


class Course(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="courses"
    )
    name = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    eligibility = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class FeeStructure(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="fee_structures"
    )
    academic_year = models.CharField(max_length=20)
    tuition_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    other_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.course.name} - {self.academic_year}"

    class Meta:
        ordering = ["-academic_year"]
