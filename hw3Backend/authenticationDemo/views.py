from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
from .models import *
import math

from django.contrib.auth.models import User

# Create your views here.
class LoginView(TemplateView):
    def get(self,request):
        users = User.objects.all
        return render(request, 'authenticationDemo/index.html', {"users": users})
    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        return render(request,"authenticationDemo/index.html")


# Create your views here.
class RegisterView(TemplateView):
    def get(self,request):
        return render(request, 'authenticationDemo/register.html')
    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        return render(request,"authenticationDemo/register.html")
