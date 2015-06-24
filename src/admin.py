from django.contrib import admin

# Register your models here.
from src.models import Event

admin.site.Register(Event)
