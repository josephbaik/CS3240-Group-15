from django.shortcuts import render, render_to_response, HttpResponseRedirect
from reportUpload.models import Report
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt


from SecureWitness import views


# Create your views here.
def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})

@csrf_exempt
def seereport(request, report_id=None):
    if not request.user.username:
        return render(request, 'login.html')
    author = str(request.user.username)

    if report_id == None:
        return render(request, 'ReportView.html', {'report': 'no report here!'})
    report = Report.objects.get(reportID=report_id)
    # print (request.POST.get('delete'))
    report.views += 1
    if request.method == 'POST':
        if request.POST.get('delete') == 'Delete':
            print('delete button has been pressed')
        if request.POST.get('edit') == 'Edit':
            print('edit button has been pressed')
        if author == report.author:
            if request.POST.get('delete') == 'Delete':
                report.delete()
                return render(request, 'ReaderHomepage.html', {'reports': Report.objects.all(), 'username': author})
            if request.POST.get('edit') == 'Edit':
                print ('rendering editreport')
                return HttpResponseRedirect('/edit/'+str(report.id))
        else:
            return render(request, 'invalidpermission.html')
    else:
        return render_to_response('ReportView.html', {'report' : Report.objects.get(reportID=report_id)})

def editreport(request, report_id):
    if not request.user.username:
        return render(request, 'login.html')
    report = Report.objects.get(pk=report_id)
    print ('entering edit report')
    if request.method == 'POST':
        print ('submit button pressed')
        title = request.POST.get('title', '')
        if title != '':
            report.title = title
        location = request.POST.get('location', '')
        if location != '':
            report.location = location
        longd = request.POST.get('longdescription', '')
        if longd != '':
            report.longd = longd
        shortd = request.POST.get('shortdescription', '')
        if shortd != '':
            report.shortd = shortd
        tags = request.POST.get('tags', '')
        if tags != '':
            report.tags = tags
        enckey = request.POST.get('enckey', '')
        if enckey != '':
            report.enckey = enckey

        author = str(request.user.username)
        folder = request.POST.get('folder', '')
        if folder != '':
            upload_dir = date.today().strftime(settings.UPLOAD_PATH) + '/' + author + '/' + folder

        report.save()
        return render(request, 'ReaderHomepage.html', {'reports': Report.objects.all() , 'firstname': request.user.username})
    
    return render(request, 'editReport.html', {'report': report, 'firstname':request.user.username})


def seemine(request):
    if not request.user.username:
        return render(request, 'login.html')
    author = str(request.user.username)
    if author == None:
        return render(request, 'myreports.html', {'reports': 'no report here!'})
    folders = []
    reports = Report.objects.filter(author=author)
    for rep in reports:
        if rep.folder not in folders:
            folders.append(rep.folder)
    return render(request, 'myreports.html', {'firstname': author, 'folders': folders, 'reports': Report.objects.filter(author=author)})



