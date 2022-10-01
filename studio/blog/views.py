
from ast import If
import re
from tokenize import Comment
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Post
from . models import Comment
from .forms import PostForm
from .forms import CommentForm
from .forms import PostDeleteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.

def home(response):
    return render(response, 'home.html', {})

class AboutUsBlog(ListView):
    model = Post
    template_name = 'about.html'

class ContactsBlog(ListView):
    model = Post
    template_name = 'contacts.html'

class FAQBlog(ListView):
    model = Post
    template_name = 'FAQ.html'

class GallaryBlog(ListView):
    model = Post
    template_name = 'gallary.html'

class BlogListView(ListView):
    model = Post
    template_name = 'blogs.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# class BlogCreateView(CreateView):
#     model = Post
#     template_name = 'blog_new.html'
#     fields = ['title', 'author', 'body']

def BlogCreateView(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post = form.save(commit=False)
            Post.author = request.user
            Post.save()
            # form.save()
            return redirect('main_post')
        else:
            error = 'Форма была неверной'

    form = PostForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog_new.html', data)

class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_edit.html'
    success_url = reverse_lazy('main_post')

# def BlogDeleteView(request,  pk):
#     if request.method == 'POST':
#         form = PostDeleteForm(request.POST)
#         if request.user == Post.user:
#             post_to_delete = Post.objects.get(id=pk)
#             post_to_delete.delete()
#             return redirect('main_post')
    
#     form = PostDeleteForm

#     data = {
#         'DeletePost':form
#     }

#     return render(request, 'blog_delete.html', data)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('main_post')




class CommentCreateview(CreateView):

    def get(__self__, request, pk):
        form = CommentForm(request.GET)
        Comment.atricle.model = Post.objects.get(pk=pk)
        error = ''
        data = {
            'Comment': form,
            'error': error
        }
        return render(request, 'comment_new.html', context=data)

    def post(__self__, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.author = request.user
            Comment.atricle = Post.objects.get(pk=pk)
            Comment.save()
            # form.save()
            return redirect('main_post')
        else:
            error = 'Форама была неверной'

        form = CommentForm()

        data = {
            'Comment': form,
            'error': error
        }
        return render(request, 'comment_new.html', data)


# def CommentCreateview(request, pk):
#     error = ''
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             Comment = form.save(commit=False)
#             Comment.author = request.user
#             Comment.save()
#             # form.save()
#             return redirect('main_post')
#         else:
#             error = 'Форама была неверной'
    
#     form = CommentForm()

#     data = {
#         'Comment':form,
#         'error': error
#     }

#     return render(request, 'comment_new.html', data)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_edit.html'
    success_url = reverse_lazy('main_post')




class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('main_post')