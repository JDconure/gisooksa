from django.contrib import admin
from django.urls import include, path
import sys
sys.path.append(r'\개인연구\config')
urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
