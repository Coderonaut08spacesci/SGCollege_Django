from django.urls import path
from . import views


urlpatterns = [
    path("notices/", views.NoticeListView.as_view(), name="notice_list"),

    path(
        "notices/<int:pk>/",
        views.NoticeDetailView.as_view(),
        name="notice_detail",
    ),

    path(
        "notices/create/",
        views.NoticeCreateView.as_view(),
        name="notice_create",
    ),

    path(
        "notices/<int:pk>/update/",
        views.NoticeUpdateView.as_view(),
        name="notice_update",
    ),

    path(
        "notices/<int:pk>/delete/",
        views.NoticeDeleteView.as_view(),
        name="notice_delete",
    ),
    
    path(
        "admission/",
        views.admission,
        name="admission",
    ),
    
    path(
        "admission/success/",
        views.admission_success,
        name="admission_success",
    ),
    
    path(
        "contact/", 
        views.contact, 
        name="contact"
    ),
        
    path(
        "contact/success/",
        views.contact_success,
        name="contact_success"
    ),
    
    path(
        "events/",
        views.event_list,
        name="event_list"
    ),
    
    path(
        "events/create/",
        views.EventCreateView.as_view(),
        name="event_create"
    ),

    path(
        "events/<int:pk>/update/",
        views.EventUpdateView.as_view(),
        name="event_update"
    ),

    path(
        "events/<int:pk>/delete/",
        views.EventDeleteView.as_view(),
        name="event_delete"
    ),
]
