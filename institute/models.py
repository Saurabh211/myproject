from django.db import models


class Institute(models.Model):

	institute_code = models.CharField(max_length=100, null=False, blank=False, default='unknown')
	institute_name = models.CharField(max_length=20, null=False, blank=False, default='unknown')
	profile_image = models.FileField(max_length=255)
	is_verified = models.BooleanField(default=False)
	is_delete = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	class Meta:
		db_table = "institute_info"



class Subject(models.Model):
	institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
	institute_class = models.CharField(max_length=20, null=False, blank=False)
	subject = models.CharField(max_length=20, null=False, blank=False)

	class Meta:
		db_table = "subject_info"


class Videos(models.Model):
	video_sub = models.ForeignKey(Subject, on_delete=models.CASCADE)
	video_url = models.CharField(max_length=20, null=False, blank=False)
	is_verified = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "video_info"
