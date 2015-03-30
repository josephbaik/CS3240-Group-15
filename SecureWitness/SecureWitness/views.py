__author__ = 'josephbaik'

from django.shortcuts import render, render_to_response, HttpResponse

def reporter(request):
    #return HttpResponse('home.html')
    return render(request, 'ReporterHomePage.html')
def admin(request):
    return render(request, 'AdminHomePage.html')
def reader(request):
    return render(request, 'ReaderHomepage.html')
#def index(request):
#    return render(request, 'login.html')
