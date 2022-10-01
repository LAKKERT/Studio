from dataclasses import field
from pyexpat import model
from turtle import title

from setuptools import Command
from .models import Post
from .models import Comment
from django.forms import ModelForm, TextInput, Select, Textarea, CharField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            "title": TextInput(attrs={
                'class': 'blog_new_input',
                'PlaceHolder': 'Название',
                'type': 'text'
            }),
            "author": Select(attrs={
                'class': 'select_author_style',
                'placeholder': 'Select Author'
            }),
            "body": Textarea(attrs={
                'class': 'textarea_newpost_style',
                'placeholder': 'write something'
            }),
        }


class PostDeleteForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author']

    

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ 'comment', 'atricle']

        widgets = {
            'comment': TextInput(attrs={
                'class': 'input_newcomment',
                'placeholder': 'НАПИШИТЕ ЧТО НИБУДЬ'
            }),
        }

