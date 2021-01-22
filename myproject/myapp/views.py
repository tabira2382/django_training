from django.views.generic import TemplateView

from .models import Post


class Index(TemplateView):
    template_name = 'myapp/index.html'

    def get_title_data(self, *args, **kwargs):
        title = super().get_context_data(**kwargs)
        post_list = Post.objects.all().order_by('-created_at')[:2]
        title = {
            'post_list': post_list,
        }
        return title
