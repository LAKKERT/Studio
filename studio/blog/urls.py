from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='main_post'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('blogs/new/', login_required(views.BlogCreateView), name='blog_new'),
    path('blogs/<int:pk>/edit/', login_required(views.BlogUpdateView.as_view()), name='blog_edit'),
    path('blogs/<int:pk>/delete/', login_required(views.BlogDeleteView.as_view()), name="blog_delete"),
    path('blogs/<int:pk>/comment/', login_required(views.CommentCreateview), name='comment_new'),
    path('blogs/comment/<int:comment_id>/commentedit/',login_required(views.CommentUpdateView.as_view()), name='comment_edit'),
    path('blogs/comment/<int:pk>/commentdel/', login_required(views.CommentDeleteView.as_view()), name='comment_del'),

]
