from django.shortcuts import render
from .models import Blog


# Create your views here.
def mon_blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/mon_blog.html', {'blogs':blogs})
