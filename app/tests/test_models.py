"""Test the models here"""

from rest_framework.test import APITestCase

from app.models import Person


class TestModels(APITestCase):
    """Test class for models"""

    def setUp(self) -> None:
        pass

    def test_person_model(self):
        """Test Person create"""

        name = "Test name"
        age = 10

        created = Person.objects.create(name=name, age=age)
        self.assertIsNotNone(created)
        self.assertEqual(Person.objects.count(), 1)
        person = Person.objects.get(id=1)
        self.assertIsNotNone(person)
        self.assertEqual(person, created)
        self.assertEqual(person.name, name)
        self.assertEqual(person.age, age)
