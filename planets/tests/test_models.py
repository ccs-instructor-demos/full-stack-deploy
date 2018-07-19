from django.test import TestCase

from planets.models import Planet


class PlanetModelTest(TestCase):
    def setUp(self):
        self.planet = Planet.objects.create(name='Hoth', description='snowy wonderland', active=True)

    def test_get_marketing_description(self):
        hoth = Planet.objects.get(name='Hoth')
        hoth_marketing_jazz = hoth.get_marketing_description()

        self.assertEquals(hoth_marketing_jazz, 'Welcome to Hoth! A snowy wonderland')

    def test_default_description(self):
        self.assertEquals(self.planet.description, 'snowy wonderland')

        no_des_planet = Planet.objects.create(name='Hoth', active=True)
        self.assertEquals(no_des_planet.description, 'Not explored yet')
