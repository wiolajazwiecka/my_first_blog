from .models import Post
from django.shortcuts import render
def post_list(request):
    wszystkie_posty=Post.objects.all()
    return render(request, 'blog/post_list.html', {"nazwa":wszystkie_posty})
# Create your views here.
