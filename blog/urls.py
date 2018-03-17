from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url("index.html/", index, name="index.html"),
    url("show_list.html/", show_blog_list, name="show_blog_list"),
    url("show_blog.html/", show_blog, name="show_blog"),
    url("add_blog.html/", add_blog, name="add_blog"),
]