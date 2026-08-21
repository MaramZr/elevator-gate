from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150, blank=True)
    company = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "question"]

    def __str__(self):
        return self.question
