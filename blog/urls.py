from django.urls import path

from .views import HomePageView, AboutPageView, ContactPageView, BlogPageView, SinglePageView, AddPostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('full-width', BlogPageView.as_view(), name='blog'),
    path('single', SinglePageView.as_view(), name='single'),
    path('add-post', AddPostView.as_view(), name='add-post')
]
