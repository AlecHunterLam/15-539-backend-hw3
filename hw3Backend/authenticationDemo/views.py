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
        # user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
        # user2 = User.objects.create_user('myusername2', 'myemai2@crazymail.com', 'mypassword2')

        users = User.objects.all
        return render(request, 'authenticationDemo/index.html', {"users": users})
    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password"]
        return render(request,"authenticationDemo/index.html")
