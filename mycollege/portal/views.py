from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Notice
from .forms import NoticeForm


class NoticeListView(ListView):
    model = Notice
    template_name = "portal/notices.html"
    context_object_name = "notices"


class NoticeDetailView(DetailView):
    model = Notice
    template_name = "portal/notice_detail.html"
    context_object_name = "notice"


class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = "portal/notice_form.html"
    success_url = reverse_lazy("notice_list")


class NoticeUpdateView(UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = "portal/notice_form.html"
    success_url = reverse_lazy("notice_list")


class NoticeDeleteView(DeleteView):
    model = Notice
    template_name = "portal/notice_confirm_delete.html"
    success_url = reverse_lazy("notice_list")
