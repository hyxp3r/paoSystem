from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Proccess1CFileForm
from .files import files1C
from .models import Tracker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import TrackerSerializer



# Create your views here.
@login_required(login_url="login")
def paoMain(request):
   return render(request, "pao/main.html")

@login_required(login_url="login")
def file(request):

   form = Proccess1CFileForm()
   
   if request.method == "POST":

      form = Proccess1CFileForm(request.POST, request.FILES)
      if form.is_valid():

         type = form.cleaned_data["types"]
         file = form.cleaned_data["file"]
         response = files1C().getInfo(file, type)
         
         if response:
            return response
         else:
            messages.info(request, "Запрос отклонен. Проверьте файл на соответствие шаблону 1С!")
      else:
            messages.info(request, "Запрос отклонен. Загрузите файл формата .xlsx!")

   return render(request,"pao/file.html", {"form":form})

@login_required(login_url="login")
def tracker(request):
   
   issue = Tracker.objects.order_by('-createdTime')[:1]
   
   return render(request, "pao/trackerIssues.html", {"issue": issue[0]})


class TrackerAPI(generics.ListAPIView):

   queryset = Tracker.objects.order_by('-createdTime')[:1]
   serializer_class = TrackerSerializer
   permission_classes = (IsAuthenticated,)