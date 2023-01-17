"""Test the views here"""

from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from app.models import Person


class TestListView(APITestCase):
    """Write test cases for app.views"""

    def setUp(self):

        name = "Test name"
        age = 10

        created = Person.objects.create(name=name, age=age)
        self.__person = created

    def _test_person(self, person: dict):

        self.assertIsInstance(person, dict)
        self.assertIn("name", person)
        self.assertIn("age", person)
        self.assertIsInstance(person["name"], str)
        self.assertIsInstance(person["age"], int)
        self.assertEqual(person["name"], self.__person.name)
        self.assertEqual(person["age"], self.__person.age)

    def test_person_detail(self):
        """Test `person/id` endpoint
        This endpoint corresponds to PersonDetailView
        """

        url = "/person/1"
        response = self.client.get(url)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, HTTP_200_OK)
        person = response.json()
        self._test_person(person=person)

    def test_person_list_view(self):
        """Test `persons/` endpoint
        This endpoint corresponds to PersonListView
        """

        url = reverse("persons")
        response = self.client.get(url)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, HTTP_200_OK)
        persons = response.json()
        self.assertIsInstance(persons, list)
        self.assertEqual(len(persons), 1)

        person = persons[0]
        self._test_person(person=person)
