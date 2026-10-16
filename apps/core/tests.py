from django.test import TestCase


class ErrorPageTests(TestCase):

    def test_404_for_unknown_url(self):
        response = self.client.get("/anything-does-not-exist/")

        self.assertEqual(response.status_code, 404)