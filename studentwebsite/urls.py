from .views import *
from django.urls import path

urlpatterns = [
	path('dashboard/', StudentDashbord.as_view(), name='dashboard'),
	path('subject/', StudentSubject.as_view(), name='subject'),
	path('<int:id>/videos/', SubjectVideos.as_view(), name='videos'),

	]