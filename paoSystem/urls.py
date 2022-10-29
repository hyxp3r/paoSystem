from django.contrib import admin
from django.urls import path, include
from pao.views import TrackerAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    path("api/v1/trackerreport/", TrackerAPI.as_view())
]
