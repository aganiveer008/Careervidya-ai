from django.db import models
from accounts.models import Category

class Course(models.Model):
    CONTENT_TYPE = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE)
    image = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    price = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    rating = models.FloatField(default=0)
    duration = models.CharField(max_length=50)
    link = models.URLField()

    is_featured = models.BooleanField(default=False)  # 🔥 YAHAN ADD

    created_at = models.DateTimeField(auto_now_add=True)
    imported_from_json = models.BooleanField(default=False)

    def __str__(self):
        return self.title