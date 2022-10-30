from django.contrib import admin
from django.urls import path, include, re_path
from pao.views import TrackerAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    path("api/v1/trackerreport/", TrackerAPI.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
