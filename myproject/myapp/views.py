from datetime import date

from django.views.generic import ListView, DetailView

from .models import Post


class Index(ListView):
    template_name = 'myapp/index.html'
    model = Post
    paginate_by = 10


class Detail(DetailView):
    template_name = 'myapp/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_date"] = date.today()
        return context
