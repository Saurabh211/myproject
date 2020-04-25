from django.contrib import admin

# Register your models here.
from login_module.models import User

admin.site.register(User)