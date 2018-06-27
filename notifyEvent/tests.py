from django.test import RequestFactory, TestCase
from . import views
from django.test import Client
import json

# Create your tests here.
'''
class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
'''

class Testviews(TestCase):
    def setup(self):
        pass

    def test_data_mensage(self):
        client = Client()
        data = {"email":"email@gmail.com",
        "segunda":"12:00 ~ 13:00 ",
        "terca":"12:00 ~ 13:00",
        "quarta":"12:00 ~ 13:00",
        "quinta":"12:00 ~ 13:00",
        "sexta":"12:00 ~ 13:00",
        "sabado":"12:00 ~ 13:00",
        "domingo":"12:00 ~ 13:00" }
        response = client.post('/notifyEvent/data_mensage',json.dumps(data), content_type="application/json")
        assert response.status_code == 200
