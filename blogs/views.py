from unicodedata import category

from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.


def posts_by_category(request, category_id):
    # Fetech the posts that belongs to the category with the id of category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = Category.objects.get(pk=category_id)
    context ={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html', context)