from django.test import TestCase


class TestWeatherViews(TestCase):

    def test_weather_page(self):
        response = self.client.get("/weather/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('weather.html')
