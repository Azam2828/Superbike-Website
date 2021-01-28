from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import About



# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is homepage")

def about(request):
   return render(request, 'about.html')

def About(request):
   return render(request, 'about.html')

def contact(request):
   if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone= request.POST.get('phone')
       desc = request.POST.get('desc')
       contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
       contact.save()
       messages.success(request, 'Congratulations! Your Response Has Been Recorded..')
   return render(request, 'contact.html')
   
def family(request):
   return render(request, 'family.html')

def services(request):
   return render(request, 'services.html')

def sportbikes(request):
   return render(request, 'sportbikes.html')

def cruiserbikes(request):
   return render(request, 'cruiserbikes.html')

def adventure(request):
   return render(request, 'adventure.html')

def touring(request):
   return render(request, 'touring.html')  

def scrambler(request):
   return render(request, 'scrambler.html') 

def caferacer(request):
   return render(request, 'caferacer.html')

def naked(request):
   return render(request, 'naked.html')       

def family(request):
   return render(request, 'family.html')   

def ducatiscrambler(request):
   return render(request, 'ducatiscrambler.html')

def hayabusa(request):
   return render(request, 'hayabusa.html')   

def privacy(request):
   return render(request, 'privacy.html')      
