from django.views.generic import ListView, DetailView

from .models import Post, Post_comment


class Index(ListView):
    template_name = 'myapp/index.html'
    model = Post
    paginate_by = 10


class Detail(DetailView):
    template_name = 'myapp/detail.html'
    model = Post_comment
