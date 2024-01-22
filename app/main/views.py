from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    blog_data = Blog.objects.all()
    context = {
        'blog_data': blog_data,
    }

    return render(request, 'home.html', context)