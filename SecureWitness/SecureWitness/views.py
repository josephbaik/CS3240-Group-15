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
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
import datetime

from SecureWitness.Encrypter import encrypt_file

from datetime import date, timedelta
import time
from reportUpload.models import Report
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



def reporter(request):
      if not request.user.username:
        return render(request, 'login.html')
      if Group.objects.get(name="admin") in request.user.groups.all():
        return render(request, 'AdminHomePage.html')
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

        tags = request.POST.get('tags') 
        enckey = request.POST.get('enckey')
        idnum = str(len(Report.objects.all())) + str(upload.name)
        if folder != "":
          address = settings.MEDIA_URL + author + '/' + folder + '/' + upload.name
        else:
          address = settings.MEDIA_URL + author + '/' + upload.name

      
        if incdate and not inctime:
          report = Report(title=request.POST['title'], author=author, date=str(date.today()), url=address, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc, tags=tags, reportID=idnum, enckey=enckey)
        if incdate and inctime:
          report = Report(title=request.POST['title'], author=author, date=str(date.today()), time=timestamp, url=address, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc, tags=tags, reportID=idnum, enckey=enckey)
        if not incdate and inctime:
          report = Report(title=request.POST['title'], author=author, time=str(timestamp), url=address, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc, tags=tags, reportID=idnum, enckey=enckey)
        if not incdate and not inctime:
          report = Report(title=request.POST['title'], author=author, url=address, short=request.POST['shortdescription'], longd=request.POST['longdescription'], location=loc, tags=tags, reportID=idnum, enckey=enckey)

        report.save()
        report.users.add(request.user)
        report.groups.add(Group.objects.get(name="admin"))

        encrypt_file(report.enckey, os.path.join(upload_full_path, upload.name+".raw"), os.path.join(upload_full_path, upload.name))

        os.remove(os.path.join(upload_dir, upload.name+".raw"))

        return render(request, 'ReporterHomePage.html')
      else:
        return render(request, 'ReporterHomePage.html')

def adm(request):
  if not request.user.username:
    return render(request, 'login.html')
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html')
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html')
  return render(request, 'invalidpermission.html')  


"""Login/User Creation Process VIEWS"""

def reader(request):
   if not request.user.username:
    return render(request, 'login.html')
   reports = Report.objects.all()
   return render(request, 'ReaderHomepage.html', {'firstname': request.user.username, 'reports': reports})


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
      return render(request, 'usercreated.html')
   else:
      raise ValidationError(password)
      return render(request, 'register.html')

def SharingPage(request):
    return render(request, 'share.html')

def shareReport(request):
    rep = False
    gro = False
    usr = False
    rpt = None
    grp = None
    us3r = None
    for g in Group.objects.all():
        if g.name == request.POST.get('group'):
            grp = g
    for u in User.objects.all():
        if u.username == request.POST.get('user'):
            us3r = u
    for r in Report.objects.all():
        if r.title == request.POST.get('report'):
            rpt = r
    if rpt == None:
        return render(request, 'share.html')
    if grp != None: 
        for g in request.user.groups.all():
            if grp.name == g.name:
                gro = True
            if g.name == "admin":
                rep = True
    if rpt.author == request.user.username:
        rep = True
    if us3r != None:
        usr = True
    if gro:
        rpt.groups.add(grp)
    if usr:
        rpt.users.add(us3r)
    return render(request, 'share.html')
        
def my_view(request):
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html')
  username = request.POST.get('username')
  password = request.POST.get('password')
  if not username or not password:
    return HttpResponseRedirect(reverse('homepage'))
  user = authenticate(username = username, password = password)
  if user is not None:
    if user.is_active:
      login(request, user)
      reports = Report.objects.all()
      return HttpResponseRedirect(reverse('Home'), {'firstname': request.user.username, 'reports': reports})         
         
    else:
      print("user is disabled")
      return render(request, 'InvalidLogin.html')


def Reportview(request, report=None):
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html')
  report = urllib
  if report == None:
    return render(request, 'ReportView.html', {'rep': 'no report here!'})
  else:
    return render(request, 'ReportView.html', {'rep': report})

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
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html')

  groupname = request.POST.get('groupname')
  if not groupname:
    return HttpResponseRedirect(reverse('newGroupPage'))
  group = Group.objects.create(name=groupname)
  user = User.objects.get(username=request.user.username)
  user.groups.add(group)
   
  return HttpResponseRedirect(reverse('addUserToGroupPage'))
  reverse('addUserToGroupPage')
  return render(request, 'addUserToGroup.html', {'groups_that_user_is_in': user.groups.all()})



def addUserToGroupPage(request):
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html') 
  user = User.objects.get(username=request.user.username)   
  return render(request, 'addUserToGroup.html', {'groups_that_user_is_in': user.groups.all()})
   




def addUserToGroup(request):
  if Group.objects.get(name="admin") in request.user.groups.all():
    return render(request, 'AdminHomePage.html')

  username = request.POST.get('username')
  groupname = request.POST.get('groupname')
   
   
  if(Group.objects.filter(name__icontains=groupname) and User.objects.filter(username__contains=username)):
    group = Group.objects.get(name=groupname)   
    user = User.objects.get(username=username)
   
    loggedinUser = User.objects.get(username = request.user.username)
   
    if group in loggedinUser.groups.all():   
      user.groups.add(group)
   
  return HttpResponseRedirect(reverse('addUserToGroupPage'))
   
   




"""-------------------CLIENT-SIDE LINKS------------------------"""


def requestgroups(request):
   list = {'groups' : []}
   for g in request.user.groups.all():
      list['groups'].append(g.name)
   return JsonResponse(list)

def requestreports(request):

   list = {'reports' : []}
   hasPrinted = False
   for g in Report.objects.all():
       for u in g.users.all():
           if u.username == request.user.username:
               list['reports'].append(g.title)
               hasPrinted = True
       if not hasPrinted:
           for u in g.groups.all():
               if u in request.user.groups.all():
                   list['reports'].append(g.title)
   return JsonResponse(list)

def requesturls(request):
   list = {}
   hasPrinted = False
   for g in Report.objects.all():
       for u in g.users.all():
           if u.username == request.user.username:
               list[g.title.encode("utf-8")] = g.url
               hasPrinted = True
       if not hasPrinted:
           for u in g.groups.all():
               if u in request.user.groups.all():
                   list[g.title.encode("utf-8")] = g.url
   return JsonResponse(list)

def requestkeys(request):
   list = {}
   hasPrinted = False
   for g in Report.objects.all():
       for u in g.users.all():
           if u.username == request.user.username:
               list[g.title.encode("utf-8")] = g.enckey
               hasPrinted = True
       if not hasPrinted:
           for u in g.groups.all():
               if u in request.user.groups.all():
                   list[g.title.encode("utf-8")] = g.enckey
   return JsonResponse(list)


"""-------------------SEARCH------------------------"""


def searchForReports(request):

   keyword = request.POST.get('query')
   tags = request.POST.get('tags')
   today = request.POST.get('today')
   last5 = request.POST.get('last5')
   last10 = request.POST.get('last10')
   lastmonth = request.POST.get('lastmonth')
   forever = request.POST.get('forever')
   q = Report.objects
   
   if not keyword and not today and not last5 and not last10 and not lastmonth and not forever and not tags:
      return HttpResponseRedirect(reverse('Home'))
   if keyword:
      q = q.filter(title__icontains=keyword)
   if tags:
      q = q.filter(tags__icontains=tags)
   if today:
      q = q.filter(date__lte=datetime.date.today())
   if last5:
      q = q.filter(date__lte=datetime.date.today()-timedelta(days=5))
   if last10:
      q = q.filter(date__lte=datetime.date.today()-timedelta(days=10))
   if lastmonth:
      q = q.filter(date__lte=datetime.date.today()-timedelta(days=30))
   if forever:
      q = q.filter(date__lte=datetime.date.today()-timedelta(days=9999))
   
   
   return render(request, 'searchResults.html', {'report_containing_keywords': q})
   
   
"""-------------GROUP AND USER LISTS-------------------"""


def listGroupsAndUsers(request):

 
   groups = request.user.groups.all()
   a = []
   for g in groups:
      a += g.user_set.all()
   return render(request, 'groupanduserlists.html', {'list_of_groups': groups, 'users': a})
   

