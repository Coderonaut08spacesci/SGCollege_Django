from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, redirect

from .forms import AdmissionForm, FeedbackForm, NoticeForm

from .models import Notice, Event, Feedback, Admission
 


class NoticeListView(ListView):
    model = Notice
    template_name = "portal/notices.html"
    context_object_name = "notices"


class NoticeDetailView(DetailView):
    model = Notice
    template_name = "portal/notice_detail.html"
    context_object_name = "notice"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return render(
                request,
                "portal/notice_not_found.html",
                status=404
            )

class NoticeCreateView(UserPassesTestMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = "portal/notice_form.html"
    success_url = reverse_lazy("notice_list")

    def test_func(self):
        return self.request.user.is_staff


class NoticeUpdateView(UserPassesTestMixin, UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = "portal/notice_form.html"
    success_url = reverse_lazy("notice_list")

    def test_func(self):
        return self.request.user.is_staff


class NoticeDeleteView(UserPassesTestMixin, DeleteView):
    model = Notice
    template_name = "portal/notice_confirm_delete.html"
    success_url = reverse_lazy("notice_list")

    def test_func(self):
        return self.request.user.is_staff
        
def admission(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("admission_success")

    else:
        form = AdmissionForm()

    return render(
        request,
        "portal/admission.html",
        {"form": form}
    )
  
def admission_success(request):
    return render(
        request,
        "portal/admission_success.html"
    )
             
def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact_success")

    else:
        form = FeedbackForm()

    return render(
        request,
        "portal/contact.html",
        {"form": form}
    )        
                
def contact_success(request):
    return render(
        request,
        "portal/contact_success.html"
    )                