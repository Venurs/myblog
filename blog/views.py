from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from django import forms

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


