from django import forms
from .models import Admission, Feedback, Notice, Event


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            "name",
            "email",
            "phone",
            "course",
            "message",
        ]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = [
            "title",
            "content",
            "category",
            "is_active",
        ]
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "date",
            "time",
            "venue",
            "image",
        ]    
