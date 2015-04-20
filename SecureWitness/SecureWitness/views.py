__author__ = 'josephbaik'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files import File
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType

from SecureWitness.Encrypter import encrypt_file

from datetime import date
from reportUpload.models import Report
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def firstscreen(request):
   return render(request, 'login.html')

def register(request):
   return render(request, 'register.html')

def addUser(request):
   username = request.POST.get('username')
   email = request.POST.get('email')
   password = request.POST.get('password')
   confirmpassword = request.POST.get('confirmpassword')
   
   if(password == confirmpassword):
      user = User.objects.create_user(username, email, password)
      
      
      permission1 = Permission.objects.get(codename='add_page')
      #permission2 = Permission.objects.get(codename='read_page')
      user.user_permissions.add(permission1)
      user.user_permissions.add(2)

      return render(request, 'usercreated.html')
   else:
      raise ValidationError(password)
      return render(request, 'register.html')

def reporter(request):
    if request.user.has_perm('SecWit.add_page') is not True:
        return render(request, 'invalidpermission.html')
    if request.method == 'POST':
        upload_dir = date.today().strftime(settings.UPLOAD_PATH)
        upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

        if not os.path.exists(upload_full_path):
            os.makedirs(upload_full_path)
        upload = request.FILES['myfile']

        while os.path.exists(os.path.join(upload_full_path, upload.name)):
            upload.name = '_' + upload.name
        dest = open(os.path.join(settings.MEDIA_ROOT, upload.name+".raw"), 'wb+')
        for chunk in upload.chunks():
            dest.write(chunk)
        dest.close()

        report = Report(title=request.POST['title'], author='bruh', date=str(date.today()), url=dest, short=request.POST['shortdescription'], longd=request.POST['longdescription'])
        report.save()

        encrypt_file("aaaaaaaaaaaaaaaa", os.path.join(settings.MEDIA_ROOT, upload.name+".raw"), os.path.join(settings.MEDIA_ROOT, upload.name))

        os.remove(os.path.join(settings.MEDIA_ROOT, upload.name+".raw"))

        return render(request, 'ReporterHomePage.html')
    else:
        return render(request, 'ReporterHomePage.html')
def adm(request):
    if request.user.has_perm('SecWit.manage_group'):
      return render(request, 'AdminHomePage.html')
    return render(request, 'invalidpermission.html')  
def reader(request):
    if request.user.has_perm('SecWit.add_page') is not True:
      return render(request, 'invalidpermission.html')
    reports = Report.objects.all()
    return render(request, 'ReaderHomepage.html')

def my_view(request):
   username = request.POST.get('username')
   password = request.POST.get('password')
   user = authenticate(username = username, password = password)
   if user is not None:
      if user.is_active:
         login(request, user)
         return render(request, 'ReaderHomepage.html', {'firstname': request.user.username})
         
      else:
         print("user is disabled")
         return render(request, 'InvalidLogin.html')

def logout_view(request):
   logout(request)
   return render(request, 'login.html')
   
