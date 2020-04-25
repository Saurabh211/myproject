from django.contrib import admin

# Register your models here.
from institute.models import *

admin.site.register(Institute)
admin.site.register(Subject)
admin.site.register(Videos)