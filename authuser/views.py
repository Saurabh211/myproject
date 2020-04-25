import requests
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from studentwebsite.models import Institute
from authuser.models import User


class Home(View):
	def get(self, request, *args, **kwargs):
		return render(request, "login/homepage.html")


class Register(View):
	def dispatch(self, request, *args, **kwargs):
		return super(Register, self).dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = request.POST
		try : institute_code = Institute.objects.get(institute_code = data['code'])
		except :
			institute_code = ''
			info = 'Invalid Institute Code'
		if institute_code:
				try:
					instance = User.objects.create_user(username = data['email'], full_name = data['full_name'], password = data['password'], standard = data['class'], institute = institute_code )
					instance.is_verified = True
					instance.save()
					info = 'success'
					try:
						group_obj = Group.objects.get(name='student')
						instance.groups.add(group_obj)
					except:
						info = 'Please select a valid class'
				except:
					info="Username already exists"
		return JsonResponse({"message": info})



class Login(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			logout(request)
		return render(request, "login/signup.html")

	def post(self, request, *args, **kwargs):
		data = request.POST
		standard = ''
		institute = ''
		try:
			user_obj = authenticate(username=data['username'], password=data['password'])
			if user_obj is not None:
				if user_obj.is_verified:
					login(request, user_obj)
					standard = user_obj.standard
					institute = user_obj.institute.institute_name
					info = 'success'
				else:
					info="Admin Verification Pending."
			else:
				info = "Invalid Username or Password."
		except:
			info = "Ops something went wrong"
		return JsonResponse({"message": info, 'standard':standard,'studentwebsite':institute }, safe=False)


class ResetPasswordForm(View):
	def get(self, request, user_id, *args, **kwargs):
		return render(request, "user/reset_password.html", {'user_id': user_id})

def logout_view(request):
	logout(request)
	return redirect('/')