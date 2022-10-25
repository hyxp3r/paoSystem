from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.paoMain, name = "paoMain"),
    path("files", views.file, name = "file" ),
    path("tracker", views.tracker, name = "tracker" ),
    
    
] 