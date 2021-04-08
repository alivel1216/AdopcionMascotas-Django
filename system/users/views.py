"""Users views."""
#Django
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView

#Models
from posts.models import Post
from django.contrib.auth.models import User

#Fomrs
from users.forms import ProfileForm, SignupForm

# Create your views here.
@login_required
def update_profile(request):
  """Update a user's profile view."""

  profile = request.user.profile

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      
      profile.website = data['website']
      profile.phone_number = data['phone_number']
      profile.biography = data['biography']
      profile.picture = data['picture']
      profile.save()

      url =reverse('users:detail',kwargs={'username': request.user.username})
      return redirect(url)
    else:
      form = ProfileForm()

  return render(
    request=request,
    template_name='users/update_profile.html',
    context={
      'profile': profile,
      'user': request.user      
    }
  )  

def login_views(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
      login(request, user)
      return redirect('posts:feed')
    else:
      return render(request, 'users/login.html', {'error': 'Invalid username or password'})
  return render(request, 'users/login.html')

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


@login_required
def logout_views(request):
  """Logout views."""
  logout(request)
  return redirect('users:login')

class UserDetailView(LoginRequiredMixin, DetailView):
  """User detail views."""
  template_name = 'users/detail.html'
  slug_field = 'username'
  slug_url_kwarg = 'username'
  queryset = User.objects.all()
  context_object_name = 'user'

  def get_context_data(self,**kwargs):
    """Add user's posts to context."""
    context = super().get_context_data(**kwargs)
    user = self.get_object()
    context['posts'] = Post.objects.filter(user=user).order_by('-create')
    return context