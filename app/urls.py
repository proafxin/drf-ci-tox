"""URL routing"""

from app import views
from django.urls import path

urlpatterns = [
    path("persons/", views.PersonListView.as_view(), name="persons"),
    path("person/<int:pk>", views.PersonDetailView.as_view(), name="person"),
]
