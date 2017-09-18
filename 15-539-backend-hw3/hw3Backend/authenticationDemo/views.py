from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
from .models import *
import math
from django.shortcuts import *
from django.contrib.auth import authenticate, login
from .models import User

# Tokens
from rest_framework.authtoken.models import Token

# View for logging into the application
class LoginView(TemplateView):
    # GET
    def get(self,request):
        # Testing/Displaying all users
        users = User.objects.all
        return render(request, 'authenticationDemo/index.html', {"users": users})
    # POST
    def post(self,request):
        # Set login credentials
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate in the database
        user = authenticate(request, username=username, password=password)
        # Validate types of login input
        if username == None or password == None or user == None:
            errorMessage = 'Invalid Credentials.'
            return render(request,"authenticationDemo/index.html",{"error":errorMessage})
        # Successful authentication of entered credentials and database
        if user.is_authenticated():
            return render(request,"authenticationDemo/profile.html",{"user":user})
        # Unsuccessful authentication of entered credentials and database
        else:
            errorMessage = 'Invalid Credentials.'
            return render(request,"authenticationDemo/index.html",{"error":errorMessage})


# View for registering an account into the application
class RegisterView(TemplateView):
    # GET
    def get(self,request):
        return render(request, 'authenticationDemo/register.html')
    # POST
    def post(self,request):
        # Testing/Displaying all users
        users = User.objects.all
        # Set inputted account information
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        # Validate account input
        if username == "" or password == "" or email == "":
            errorMessage = 'Invalid Input for User Credentials.'
            return render(request,"authenticationDemo/register.html",{"error":errorMessage})
        # Save user into database
        user = User.objects.create_user(username, email, password)
        # Set token for the new user
        Token.objects.create(user=user)
        # Redirect to login page after successful account creation
        return redirect("../..", {"users":users})
