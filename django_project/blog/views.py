from django.shortcuts import render, get_object_or_404
from .models import Posts


def post_list(request):
    post1 = Posts.objects.all()
    return render(request, 'home.html', {'posts': post1})

def post_detail(request, pk): # new
    post = get_object_or_404(Posts, pk=pk)
    return render(request, "post_detail.html", {"post": post})