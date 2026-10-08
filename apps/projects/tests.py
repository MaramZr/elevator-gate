from django.test import TestCase
from django.urls import reverse

from apps.services.models import Service
from .models import Project, ProjectCategory


class ProjectViewTests(TestCase):

    def setUp(self):
        self.service = Service.objects.create(
            title="صيانة المصاعد",
            slug="elevator-maintenance",
            description="خدمة صيانة المصاعد",
        )

        self.category = ProjectCategory.objects.create(
            name="Residential",
            slug="residential",
        )

        self.other_category = ProjectCategory.objects.create(
            name="Commercial",
            slug="commercial",
        )

        self.project = Project.objects.create(
            title="مشروع برج سكني",
            slug="residential-tower",
            category=self.category,
            service=self.service,
        )

        self.other_project = Project.objects.create(
            title="مشروع تجاري",
            slug="commercial-project",
            category=self.other_category,
            service=self.service,
        )

    def test_project_detail_by_slug(self):
        response = self.client.get(
            reverse(
                "projects:project_detail",
                kwargs={"slug": self.project.slug},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["project"],
            self.project
        )

    def test_project_list_filters_by_category(self):
        response = self.client.get(
            reverse("projects:project_list"),
            {"category": self.category.slug},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)
        self.assertNotContains(response, self.other_project.title)