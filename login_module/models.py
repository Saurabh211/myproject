from django.contrib.auth.models import AbstractUser, User
from django.db import models
from institute.models import Institute


class User(AbstractUser):
	institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100, null=False, blank=False, default='unknown')
	mobile_number = models.CharField(max_length=20, null=False, blank=False, default='unknown')
	standard = models.CharField(max_length=20, null=False, blank=False, default='unknown')
	is_verified = models.BooleanField(default=False)
	is_delete = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	class Meta:
		db_table = "user_info"