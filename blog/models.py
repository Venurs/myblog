from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, default="博客题目未设置")
    author = models.CharField(max_length=30)
    mktime = models.DateTimeField()
    classify = models.ForeignKey("Classify", on_delete=models.CASCADE)
    abstract = models.CharField(max_length=200)
    content = HTMLField()


class Classify(models.Model):
    name = models.CharField(max_length=10)
