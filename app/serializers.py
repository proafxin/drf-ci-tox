"""Define serializers"""

from app import models
from rest_framework.serializers import ModelSerializer


class PersonSerializer(ModelSerializer):
    """Serializer for Person model"""

    class Meta:
        """Specify fields for Person"""

        model = models.Person
        fields = "__all__"
