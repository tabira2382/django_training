from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
]
