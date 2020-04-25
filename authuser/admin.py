from django.contrib import admin

# Register your models here.
from authuser.models import User

admin.site.register(User)