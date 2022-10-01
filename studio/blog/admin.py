from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post
from .models import Comment
# Register your models here.

from . import models 

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Post, ArticleAdmin)
admin.site.register(models.Comment)
