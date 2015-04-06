__author__ = 'josephbaik'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files import File
from django.shortcuts import render_to_response
from django.conf import settings

from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def reporter(request):
    if request.method == 'POST':
        upload_dir = date.today().strftime(settings.UPLOAD_PATH)
        upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

        if not os.path.exists(upload_full_path):
            os.makedirs(upload_full_path)
        upload = request.FILES['myfile']

        while os.path.exists(os.path.join(upload_full_path, upload.name)):
            upload.name = '_' + upload.name
        dest = open(os.path.join(settings.MEDIA_ROOT, upload.name), 'wb+')
        for chunk in upload.chunks():
            dest.write(chunk)
        dest.close()

        return render(request, 'ReporterHomePage.html')
    else:
        return render(request, 'ReporterHomePage.html')
def adm(request):
    return render(request, 'AdminHomePage.html')
def reader(request):
    return render(request, 'ReaderHomepage.html')
def login(request):
    return render(request, 'login.html')

def handle_uploads(request, keys):
    saved = []

    upload_dir = date.today().strftime(settings.UPLOAD_PATH)
    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)

    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)

    for key in keys:
        if key in request.FILES:
            upload = request.FILES[key]
            while os.path.exists(os.path.join(upload_full_path, upload.name)):
                upload.name = '_' + upload.name
            dest = open(os.path.join(upload_full_path, upload.name), 'wb')
            for chunk in upload.chunks():
                dest.write(chunk)
            dest.close()
            saved.append((key, os.path.join(upload_dir, upload.name)))
    # returns [(key1, path1), (key2, path2), ...]
    return saved
