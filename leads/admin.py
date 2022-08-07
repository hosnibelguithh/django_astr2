from django.contrib import admin

from accounts.views import register
from .models import Prospect, Event
# Register your models here.

admin.site.register(Prospect)
admin.site.register(Event)

