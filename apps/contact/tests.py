from django.test import TestCase
from django.urls import reverse

from apps.contact.models import ContactMessage


# Create your tests here.

class ContactViewTests(TestCase):

    def test_contact_page_returns_200(self):
        response = self.client.get(
            reverse("contact:contact")
        )


        self.assertEqual(response.status_code, 200)


    def test_contact_without_privacy_consent(self):
        response = self.client.post(
            reverse("contact:contact"),

            data = {
                "name": "Test User",
                "email": "test@example.com",
                "subject": "Test Subject",
                "message": "This is a test message.",
            }

        )

        self.assertEqual(ContactMessage.objects.count(),0)

    def test_contact_with_privacy_consent(self):
        response = self.client.post(
            reverse("contact:contact"),

            data = {
                "name": "Test User",
                "email": "test@example.com",
                "subject": "Test Subject",
                "message": "This is a test message.",
                "privacy": "on",
            }
        )

        self.assertEqual(ContactMessage.objects.count(),1)
        self.assertRedirects(response, reverse("contact:success"))

    def test_contact_with_invalid_email(self):

    # Arrange
        data = {
            "name": "Maram",
            "email": "maram-invalid-email",
            "subject": "Maintenance Request",
            "message": "I need elevator maintenance.",
            "privacy": "on",
        }

        # Act
        response = self.client.post(
            reverse("contact:contact"),
            data=data
        )

        # Assert
        #   Assertion تتأكد أن status_code يساوي 200
        self.assertEqual(response.status_code, 200)

        #  Assertion تتأكد أن عدد الرسائل يساوي 0
        self.assertEqual(ContactMessage.objects.count(), 0)

        self.assertFormError(
            response.context["form"],
            "email",
            "أدخِل عنوان بريد إلكتروني صحيح."
        )


    def test_contact_rejects_invalid_privacy_value(self):
        data = {
                    "name": "Maram",
                    "email": "test@example.com",
                    "subject": "Maintenance Request",
                    "message": "I need elevator maintenance.",
                    "privacy": "false",
                }
        response = self.client.post(reverse("contact:contact"), data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

