from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns=[
    path('',blog_home_view,name='blog-home'),
    path('<int:pid>',blog_single_view,name='blog-single'),
    path('search/',blog_search,name="search"),
    path('category/<str:cat_name>',blog_home_view,name='category'),
    path('tag/<str:tag_name>',blog_home_view,name='tags'),
    path('Author/<str:author_username>',blog_home_view,name='author'),
]