from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
from .models import *
import math

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
class LoginView(TemplateView):
    def get(self,request):
        users = User.objects.all
        return render(request, 'authenticationDemo/index.html', {"users": users})

    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if username == None or password == None or user == None:
            errorMessage = 'Invalid Credentials.'
            return render(request,"authenticationDemo/index.html",{"error":errorMessage})
        if user.is_authenticated():
            return render(request,"authenticationDemo/profile.html",{"user":user})
        else:
            errorMessage = 'Invalid Credentials.'
            return render(request,"authenticationDemo/index.html",{"error":errorMessage})


# Create your views here.
class RegisterView(TemplateView):
    def get(self,request):
        return render(request, 'authenticationDemo/register.html')
    def post(self,request):
        users = User.objects.all
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        if username == None or password == None or email == None:
            errorMessage = 'Invalid Input for User Credentials.'
            return render(request,"authenticationDemo/register.html",{"error":errorMessage})

        user = User.objects.create_user(username, email, password)


        return render(request,"authenticationDemo/index.html", {"users":users})
