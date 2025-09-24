# edusync360/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token  # 👈 import view
from accounts.views import CustomAuthToken

def home(request):
    return HttpResponse("Welcome to EduSync-360 Backend API 🚀")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),   # core app urls
    path("api-auth/", include("rest_framework.urls")),  # browsable API login
    path("api/token-auth/", obtain_auth_token, name="api_token_auth"),  # 👈 fixed
    path("login/", CustomAuthToken.as_view(), name="api_login"),
    path("api/accounts/", include("accounts.urls")),
    path('api/', include('students.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
