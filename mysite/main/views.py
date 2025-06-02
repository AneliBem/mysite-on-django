from django.shortcuts import render, get_object_or_404
from .models import Category

def categories(request, category_slug=None):
    categories = Category.objects.all()

    category = None
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        
    return render(request, 'base.html',
                  {'category': category,
                   'categories': categories})



