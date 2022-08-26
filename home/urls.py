from django.urls import path
from django.contrib import admin
import sys
sys.path.append(r'\config\home')
from .views import index, detail
app_name='home'
urlpatterns = [
    # ex: /home/
    path('', index, name='index'),
    # ex: /home/5/
    path('<int:person_id>/', detail, name='detail'),
]