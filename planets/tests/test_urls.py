import json

# from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from rest_framework.test import APIClient
from model_mommy import mommy

from planets.models import Planet


class PlanetViewSetTest(TestCase):
    def setUp(self):
        self.planet = mommy.make(Planet)

    def test_planet_list(self):
        # Make sure the rest framework router is configured
        url = reverse('planet-list')
        self.assertEqual(url, '/testing-url/api/planets/')

        # Functional test: get list of planets
        c = Client()
        response = c.get(reverse('planet-list'), content_type='application/json')
        self.assertEquals(200, response.status_code)

    def test_planet_detail(self):
        # Make sure the rest framework router is configured
        url = reverse('planet-detail', kwargs={'pk': self.planet.pk})
        self.assertEqual(url, '/testing-url/api/planets/{}/'.format(self.planet.pk))

        # Functional test: get detail of planet
        c = Client()
        response = c.get(reverse('planet-detail', kwargs={'pk': self.planet.pk}), content_type='application/json')
        self.assertEquals(200, response.status_code)

    def test_planet_create(self):
        # Functional test: get detail of planet
        c = APIClient()
        planet_data = {
            'name': 'Endor',
            'description': 'sanctuary moon',
            'banner_image': None,
            'active': True,
        }

        # Post request should create record and return status 201
        response = c.post(reverse('planet-list'), planet_data, format='json')
        self.assertEquals(201, response.status_code)

        # Convert json response to dict and remove the id since we don't know what its value is
        response_data = json.loads(response.content)
        response_data.pop('id')

        # API should not return active field in response
        planet_data.pop('active')

        # Make sure the planet was created with the values we provided
        self.assertEquals(response_data, planet_data)
