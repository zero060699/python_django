from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Post
from django.http import Http404
from django.views.generic import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1
def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")
    return render(request, 'blog/post.html',{'post': post})
    
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url