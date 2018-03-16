from django.contrib import admin
from blog.models import *
from tinymce.models import *
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "mktime", "abstract", "classify_id")


@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

