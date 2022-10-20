
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User

# Create your views here.

def main(request):
   if request.user.is_authenticated:
      return redirect("home")
   else:
      return redirect("login")

@login_required(login_url = 'login')
def home (request):
   
   return render(request, "paoSystem/home.html")


def userAuth(request):

   if request.user.is_authenticated:
      return redirect("home")


   if request.method == "POST":

      username = request.POST.get("login")
      password = request.POST.get("password")
      user = authenticate(request, username = username, password = password)

      if user is not None:
         login(request, user)
         return redirect("home")
      else:
         messages.info(request, "Имя пользователя или пароль не верны")

   return render(request, "paoSystem/auth.html" )

def user_logout(request):
   logout(request)
   return redirect("login")

