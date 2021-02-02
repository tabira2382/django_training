from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentForm, LoginForm
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


class Login(LoginView):
    template_name = 'myapp/login.html'
    form_class = LoginForm
