from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CommentForm
from .models import Post, Post_comment


class Index(ListView):
    template_name = 'myapp/index.html'
    model = Post
    paginate_by = 10


class Detail(DetailView):
    template_name = 'myapp/detail.html'
    model = Post


class CommentCreate(CreateView):
    template_name = 'myapp/post_comment_form.html'
    model = Post_comment
    form_class = CommentForm
    success_url = reverse_lazy('myapp:detail')

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        post_comment = self.model()
        Post_comment = form.save(commit=False)
        post_comment.post = Post.objects.get(pk=post_pk)
        post_comment.comment = Post_comment
        post_comment.save()
        return redirect('myapp:detail', pk=post_pk)


class CommentUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'myapp/update.html'
    model = Post_comment
    form_class = CommentForm
    success_url = reverse_lazy('myapp:detail')

    def get_success_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.object.pk})
