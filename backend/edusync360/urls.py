from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',include('students.urls')),
    path('teachers/',include('teachers.urls')),
    path('adminpanel/',include('adminpanel.urls')),
    path('core/',include('core.urls'))
]
