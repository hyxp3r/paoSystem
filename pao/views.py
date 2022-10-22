from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def paoMain(request):
   return render(request, "pao/trackerIssues.html")

@login_required(login_url="login")
def file(request):

   if request.method == "POST":
      username = request.POST.get("flexRadioDefault").value()
      print(username)

   return render(request,"pao/file.html")