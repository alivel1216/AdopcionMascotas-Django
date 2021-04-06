"""Users views."""
#Djano
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Exceptions
from django.db.utils import IntegrityError
#models
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
@login_required
def update_profile(request):
  """Update a user's profile view."""
  return render(request,'users/update_profile.html')

def login_views(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
      login(request, user)
      return redirect('feed')
    else:
      return render(request, 'users/login.html', {'error': 'Invalid username or password'})
  return render(request, 'users/login.html')

def signup_views(request):
  """Sign up views."""
  if request.method=='POST':
    username = request.POST['username']
    passwd = request.POST['passwd']
    passwd_confirmation = request.POST['passwd_confirmation']
    if passwd != passwd_confirmation:
      return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})

    try:
      user = User.objects.create_user(username=username,password=passwd)
    except IntegrityError:
      return render(request,'users/signup.html',{'error':'Username is already in use'})
    
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    profile = Profile(user=user)
    profile.save()
    return redirect('login')

  return render(request, 'users/signup.html')

@login_required
def logout_views(request):
  """Logout views."""
  logout(request)
  return redirect('login')
