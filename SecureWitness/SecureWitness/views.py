__author__ = 'josephbaik'

from django.shortcuts import render, render_to_response, HttpResponse

def index(request):
    #return HttpResponse('home.html')
    return render(request, 'ReporterHomePage.html')