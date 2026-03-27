from django.core.management.base import BaseCommand
import json
from courses.models import Course
from accounts.models import Category

class Command(BaseCommand):
    help = 'Import courses from JSON file using existing categories only'

    def handle(self, *args, **kwargs):
        with open('courses.json', 'r') as f:
            data = json.load(f)

        # Get all existing categories from admin
        existing_categories = {c.name.lower(): c for c in Category.objects.all()}

        for item in data:
            cat_name = item['category'].strip().lower()  # normalize
            cat = existing_categories.get(cat_name)

            if not cat:
                # Category not in admin, skip course or warn
                self.stdout.write(self.style.WARNING(
                    f"Category '{item['category']}' not found in admin. Skipping course '{item['title']}'"
                ))
                continue  # Skip this course

            # Import course
            course, created = Course.objects.get_or_create(
                title=item['title'],
                defaults={
                    'description': item['description'],
                    'content_type': item['content_type'],
                    'image': item.get('image'),
                    'video_url': item.get('video_url'),
                    'price': item['price'],
                    'category': cat,
                    'level': item['level'],
                    'rating': item['rating'],
                    'duration': item['duration'],
                    'link': item['link'],
                    'is_featured': item['is_featured'],
                }
            )

            if not created:
                # update existing course
                course.description = item['description']
                course.content_type = item['content_type']
                course.image = item.get('image')
                course.video_url = item.get('video_url')
                course.price = item['price']
                course.category = cat
                course.level = item['level']
                course.rating = item['rating']
                course.duration = item['duration']
                course.link = item['link']
                course.is_featured = item['is_featured']
                course.save()

        self.stdout.write(self.style.SUCCESS('Courses Imported Successfully 🚀'))