from django.contrib import admin
from .models import Notice, Event, Feedback, Admission


admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Feedback)
admin.site.register(Admission)