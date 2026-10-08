from django.test import TestCase
from django.urls import reverse
from .models import Service, ServiceFeature


# Create your tests here.

class ServiceModelTestCase(TestCase):
    
    def test_service_creation(self):
        service = Service.objects.create(title="صيانة المصاعد",
        slug="elevator-maintenance",
        description="خدمة صيانة المصاعد",
        )

        self.assertEqual(Service.objects.count(), 1)
        self.assertEqual(str(service), "صيانة المصاعد")

    def test_service_feature_relationship(self):
        service = Service.objects.create(
            title="صيانة المصاعد",
            slug="elevator-maintenance",
            description="خدمة صيانة المصاعد",

        )  

        feature = ServiceFeature.objects.create(
            service=service,
            title="فحص شامل",
            description="فحص شامل لجميع أجزاء المصعد",
        )
        self.assertEqual(service.features.count(), 1) 

    def test_service_detail_by_slug(self):
        service = Service.objects.create(
            title="صيانة المصاعد",
            slug="elevator-maintenance",
            description="خدمة صيانة المصاعد",
        )

        response = self.client.get(
            reverse(
                "services:service_detail",
                kwargs={"slug": service.slug}
            )
        )
        self.assertEqual(response.status_code, 200)
        