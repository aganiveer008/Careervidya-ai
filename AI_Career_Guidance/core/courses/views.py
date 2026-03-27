from django.shortcuts import render
from .models import Course
from accounts.models import Category

def course_list(request):
    courses = Course.objects.all()
    categories = Category.objects.all()

    # Search
    query = request.GET.get('q')
    if query:
        courses = courses.filter(title__icontains=query)

    # Filter by category
    category = request.GET.get('category')
    if category:
        courses = courses.filter(category__name=category)

    # Filter by level
    level = request.GET.get('level')
    if level:
        courses = courses.filter(level=level)

    context = {
        'courses': courses,
        'categories': categories,

    }
    return render(request, 'accounts/courses.html', context)