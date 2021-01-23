from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("About",views.About, name='About'),
    path("contact",views.contact, name='contact'),
    path("services",views.services, name='services'),
    path("sportbikes",views.sportbikes, name='sportbikes'),
    path("cruiserbikes",views.cruiserbikes, name='cruiserbikes'),
    path("adventure",views.adventure, name='adventure'),
    path("family",views.family, name='family'),
    path("bounvile",views.bounvile, name='bounvile'),
    path("hayabusa",views.hayabusa, name='hayabusa'),
    path("privacy",views.privacy, name='privacy')
    
   
    
]