from django.test import TestCase


class TestAboutViews(TestCase):

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('about.html')
