from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
import math

# Create your views here.
class LoginView(TemplateView):
    def get(self,request):
        return render(request, 'authenticationDemo/index.html')
    def post(self,request): 
        return render(request,"authenticationDemo/index.html")
