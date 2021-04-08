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
    paginate_by = 2
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

def listar_publicaciones(request):
    busqueda = request.POST.get("buscar") #Recuperamos la busqueda del usuario 
    autores = Post.objects.all()
    
   
    if busqueda: #Preguntando si busqueda está llena 
        category = Post.objects.filter(
            Q(category = busqueda) 
        ).distinct()
    return render(request, 'posts/feed.html')

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