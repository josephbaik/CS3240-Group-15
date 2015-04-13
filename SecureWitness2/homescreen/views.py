from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your views here.


def my_view(request):
   username = request.POST.get('username')
   password = request.POST.get('password')
   user = authenticate(username = username, password = password)
   if user is not None:
      if user.is_active:
         login(request, user)
         return render(request, 'ReaderHomepage.html')
         
      else:
         print("user is disabled")
         return render(request, 'InvalidLogin.html')
      
   else:
      print("user is incorrect")
      return render(request, 'login.html')
      
def firstscreen(request):
   return render(request, 'login.html')
      
def reader(request):
   return render(request, 'ReaderHomepage.html')
    
def register(request):
   return render(request, 'register.html')
   
def addUser(request):
   username = request.POST.get('username')
   email = request.POST.get('email')
   password = request.POST.get('password')
   confirmpassword = request.POST.get('confirmpassword')
   
   if(password == confirmpassword):
      user = User.objects.create_user(username, email, password)
      return render(request, 'usercreated.html')
   else:
      raise ValidationError(password)
      return render(request, 'register.html')
      
   
   
   