from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('home/', blog_views.home, name='blog-home'),
    path('about/', blog_views.about, name='blog-about'),
    path('contactus/', blog_views.contactus, name='blog-contactus'),
]