"""Define views"""

from rest_framework import generics

from app import models, serializers


class PersonListView(generics.ListCreateAPIView):
    """Class based list view for Person"""

    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Class based detail view for Person"""

    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()
