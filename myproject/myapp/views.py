from django.views.generic import ListView

from .models import Post


class Index(ListView):
    template_name = 'myapp/index.html'
    model = Post
    paginate_by = 10
