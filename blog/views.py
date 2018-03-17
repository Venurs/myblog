from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from django import forms
import markdown
import datetime

# Create your views here.


"""class BlogForm(forms.Form):
    title = forms.CharField(max_length=200, widget=MarkdownWidget)
    author = forms.CharField(max_length=30, widget=MarkdownWidget)
    mktime = forms.DateTimeField()
    abstract = forms.CharField(max_length=200, widget=MarkdownWidget)
    content = MarkdownFormField()"""


def index(request):
    return render(request, "blog/index.html", {})


def show_blog_list(request):
    return render(request, "blog/show_blog_list.html", {})


def show_blog(request):
    blog = Blog.objects.get(pk=3)
    blog.content = markdown.markdown(blog.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
    ])
    return render(request, "blog/show_blog.html", {"blog": blog})


def add_blog(request):
    if request.method == "GET":
        return render(request, "blog/add_blog.html", {})
    elif request.method == "POST":
        title = request.POST.get("title")
        mktime = datetime.datetime.now()
        abstract = request.POST.get("abstract")
        content = request.POST.get("content")
        print(mktime)
        # print(title, abstract, content)
        return render(request, "blog/index.html", {})


