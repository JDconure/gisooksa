from django.contrib import admin
import sys
sys.path.append(r'\개인연구\config\home')
from .models import Person
admin.site.register(Person)