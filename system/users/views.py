"""Users views."""
#Djano
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.

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