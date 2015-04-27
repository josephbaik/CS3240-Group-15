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
    author = str(request.user.username)

    if report_id == None:
        return render(request, 'ReportView.html', {'report': 'no report here!'})
    report = Report.objects.get(reportID=report_id)
    # print (request.POST.get('delete'))
    if request.method == 'POST':
        print('button has been pressed')
        if author == report.author:
            report.delete()
            return render(request, 'ReaderHomepage.html', {'reports': Report.objects.all(), 'username': author})
        else:
            return render(request, 'invalidpermission.html')
    else:
        return render_to_response('ReportView.html', {'report' : Report.objects.get(reportID=report_id)})


def seemine(request):
    author = str(request.user.username)
    if author == None:
        return render(request, 'myreports.html', {'reports': 'no report here!'})

    return render(request, 'myreports.html', {'firstname': author, 'reports': Report.objects.filter(author=author)})