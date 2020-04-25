from django.shortcuts import render
from django.views import View

from institute.models import *


class StudentDashbord(View):
	def get(self, request, *args, **kwargs):
		return render(request, "institute/dashbord.html")


class StudentSubject(View):
	def get(self, request, *args, **kwargs):
		subject = Subject.objects.filter(institute = request.user.institute , institute_class = request.user.standard)
		return render(request, "institute/subject.html", {'subject':subject})


class SubjectVideos(View):
	def get(self, request, id):
		videos = Videos.objects.filter(video_sub__id = id )
		return render(request, "institute/videos.html", {'videos' : videos})