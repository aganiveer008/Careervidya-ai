from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = 'Delete all courses'

    def handle(self, *args, **kwargs):
        Course.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All courses deleted successfully 🗑️'))