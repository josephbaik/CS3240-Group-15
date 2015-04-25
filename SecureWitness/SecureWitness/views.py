__author__ = 'josephbaik'

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files import File
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from SecureWitness.Encrypter import encrypt_file

from datetime import date
import time
from reportUpload.models import Report
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



def reporter(request):
    if request.user.has_perm('SecWit.add_page') is not True:
        return render(request, 'invalidpermission.html')
    if request.method == 'POST':
        author = str(request.user.username)
        folder = request.POST.get('folder', '')
        upload_dir = date.today().strftime(settings.UPLOAD_PATH) + '/' + author + '/' + folder
        upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)
        if not os.path.exists(upload_full_path):
            os.makedirs(upload_full_path)
            upload = request.FILES['myfile']

        while os.path.exists(os.path.join(upload_full_path, upload.name)):
            upload.name = '_' + upload.name
        dest = open(os.path.join(upload_full_path, upload.name+".raw"), 'wb+')
        print (str(dest))
        for chunk in upload.chunks():
            dest.write(chunk)
        dest.close()

        reportdest = os.path.join(upload_full_path, author + '/' + folder + '/' + upload.name+".raw")
        incdate = request.POST.get('date', False)
        inctime = request.POST.get('time', False)
        loc = request.POST.get('location', 'none')

        timestamp = time.ctime()

        if incdate and not inctime:
            report = Report(title=request.POST['title'], author=author, date=str(date.today()), url=upload_full_path, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc)
        if incdate and inctime:
            report = Report(title=request.POST['title'], author=author, date=str(date.today()), time=timestamp, url=upload_full_path, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc)
        if not incdate and inctime:
            report = Report(title=request.POST['title'], author=author, time=str(timestamp), url=upload_full_path, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc)
        if not incdate and not inctime:
            report = Report(title=request.POST['title'], author=author, url=upload_full_path, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc)

        report.save()

        encrypt_file("aaaaaaaaaaaaaaaa", os.path.join(upload_full_path, upload.name+".raw"), os.path.join(upload_full_path, upload.name))

        os.remove(os.path.join(upload_dir, upload.name+".raw"))

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
    return render(request, 'ReaderHomepage.html', {'reports': reports})




"""Login/User Creation Process VIEWS"""

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


def my_view(request):
   username = request.POST.get('username')
   password = request.POST.get('password')
  
   user = authenticate(username = username, password = password)
   if user is not None:
      if user.is_active:
         login(request, user)
         reports = Report.objects.all()
         return render(request, 'ReaderHomepage.html', {'firstname': request.user.username, 'reports': reports})
         
      else:
         print("user is disabled")
         return render(request, 'InvalidLogin.html')

def Reportview(request):
  return render(request, 'ReportView.html')

def logout_view(request):
   logout(request)
   return render(request, 'login.html')

@csrf_exempt   
def login_user(request):
   username = request.POST['username']
   password=request.POST['password']
   user = authenticate(username=username, password=password)
   login(request, user)
   return render(request, 'ReaderHomepage.html', {'firstname': request.user.username})



"""-------------Create/Manage Groups-------------------"""

def newGroupPage(request):
   return render(request, 'createGroup.html')
   


def createGroup(request):

   groupname = request.POST.get('groupname')
   
   group = Group.objects.create(name=groupname)
   user = User.objects.get(username=request.user.username)
   user.groups.add(group)
   return render(request, 'addUserToGroup.html')



def addUserToGroupPage(request):
   return render(request, 'addUserToGroup.html')


def addUserToGroup(request):


   username = request.POST.get('username')
   groupname = request.POST.get('groupname')
   
   group = Group.objects.get(name=groupname)
   
   user = User.objects.get(username=username)
   
   user.groups.add(group)
   
   return render(request, 'addUserToGroup.html')
   




"""------------------------------------------------"""


def requestgroups(request):
   list = {'groups' : []}
   print(request.user.username)
   for g in request.user.groups.all():
      list['groups'].append(g.name)
   return JsonResponse(list)

def requestreports(request):
   list = {'reports' : []}
   print(request.user.username)
   for g in Report.objects.all():
      for u in g.users.all():
         print(u.username)
         if u.username == request.user.username:
            list['reports'].append(g.title)
   return JsonResponse(list)
