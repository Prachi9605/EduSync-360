# edusync360/urls.py (project-level)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to EduSync-360 Backend API 🚀")

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),   # if using core router
    # optional: token auth endpoint
    path("api-auth/", include("rest_framework.urls")),  # browsable API login
    path("api/token-auth/", include("rest_framework.authtoken.views")),  # alternative (see note)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
