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
    path("touring",views.touring, name='touring'),
    path("scrambler",views.scrambler, name='scrambler'),
    path("caferacer",views.caferacer, name='caferacer'),
    path("naked",views.naked, name='naked'),
    path("family",views.family, name='family'),
    path("ducatiscrambler",views.ducatiscrambler, name='ducatiscrambler'),
    path("hayabusa",views.hayabusa, name='hayabusa'),
    path("privacy",views.privacy, name='privacy')
    
   
    
]
