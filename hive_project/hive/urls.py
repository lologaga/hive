from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hive-home'),
    # apply my view 'home' to the blog/urls.py for user

    path('about/', views.about, name='hive-about'),
    # apply my view 'about' to the blog/urls.py for user in the directory about/ it means http://127.0.0.1:8000/about
]