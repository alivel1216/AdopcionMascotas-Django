#Post/views
#Dajngo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q

from posts.forms import PostForm

#Models 
from posts.models import Post



class PostsFeedView(LoginRequiredMixin, ListView):
    """List existing posts"""
   
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-create',)
    paginate_by = 6
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

def GuiaAdopcionView(request):
    """Return post detail."""
    return render(request, 'posts/guia.html')