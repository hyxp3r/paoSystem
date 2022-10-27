from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("", views.paoMain, name = "paoMain"),
    path("files/1C", views.file, name = "file1C" ),
    path("tracker", views.tracker, name = "trackerDash" ),
    
    
] 