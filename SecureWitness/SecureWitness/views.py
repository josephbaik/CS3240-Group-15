__author__ = 'josephbaik'

from django.shortcuts import render
def reporter(request):
    return render(request, 'ReporterHomePage.html')
def adm(request):
    return render(request, 'AdminHomePage.html')
def reader(request):
    return render(request, 'ReaderHomepage.html')
