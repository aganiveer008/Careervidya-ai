from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'price', 'is_featured', 'rating')
    list_filter = ('category', 'level', 'is_featured')
    search_fields = ('title', 'description')
    list_editable = ('is_featured', 'price')
