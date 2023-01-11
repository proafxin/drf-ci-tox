"""Define serializers"""

from rest_framework.serializers import ModelSerializer

from app import models


class PersonSerializer(ModelSerializer):
    """Serializer for Person model"""

    class Meta:
        """Specify fields for Person"""

        model = models.Person
        fields = "__all__"
