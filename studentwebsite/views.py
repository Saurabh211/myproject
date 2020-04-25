from django.shortcuts import render
from django.views import View

from studentwebsite.models import *


class StudentDashbord(View):
	def get(self, request, *args, **kwargs):
		return render(request, "studentwebsite/dashbord.html")


class StudentSubject(View):
	def get(self, request, *args, **kwargs):
		subject = Subject.objects.filter(institute = request.user.institute , institute_class = request.user.standard)
		return render(request, "studentwebsite/subject.html", {'subject':subject})


class SubjectVideos(View):
	def get(self, request, id):
		videos = Videos.objects.filter(video_sub__id = id )
		return render(request, "studentwebsite/videos.html", {'videos' : videos})