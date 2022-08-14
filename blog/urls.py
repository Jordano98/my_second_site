from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns=[
    path('',blog_home_view,name='blog-home'),
    path('blog-single',blog_single_view,name='blog-single'),
    path('search/',blog_search,name="search"),
]