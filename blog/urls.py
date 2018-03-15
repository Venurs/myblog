from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url("index.html/", index, name="index.html"),
    url("show_list.html/", show_blog_list, name="show_blog_list"),
]