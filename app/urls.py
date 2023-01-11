"""URL routing"""

from django.urls import path

from app import views

urlpatterns = [
    path("persons/", views.PersonListView.as_view(), name="persons"),
    path("person/<int:pk>", views.PersonDetailView.as_view(), name="person"),
]
