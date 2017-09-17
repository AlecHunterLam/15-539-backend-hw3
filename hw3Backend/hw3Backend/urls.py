"""hw3Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from authenticationDemo import views

# URLS for authentication app
urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    # Login URL
    url(r'^$', views.LoginView.as_view(),name='login'),
    # Registration URL
    url(r'^register/', views.RegisterView.as_view(),name='register'),
    # rest_framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
