from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('comment_create/<int:pk>', views.CommentCreate.as_view(), name='comment_create'),
    path('login', views.Login.as_view(), name='login')
]
