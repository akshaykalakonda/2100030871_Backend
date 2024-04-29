"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.country, name="country"),
    path('country',views.country,name="country"),
    path('addcountry',views.addcountry,name='addcountry'),
    path('displaycountry', views.displaycountry,name='displaycountry'),
    path('addloc',views.addloc,name='addloc'),
    path('addLocation',views.addLocation, name='addLocation'),
    path('add_location',views.add_location,name='add_location'),
    path('display_locations',views.display_locations,name='display_locations'),
    path('canada_addresses',views.canada_addresses,name='canada_addresses'),
    path('canada_address',views.canada_address,name='canada_address'),
]
