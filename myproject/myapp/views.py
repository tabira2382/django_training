from django.views.generic import TemplateView

from .models import Post


class Index(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        post_list = Post.objects.all().order_by('-created_at')[:2]
        context = {
            'post_list': post_list,
        }
        return context
