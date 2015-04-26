from django.shortcuts import render, render_to_response
from reportUpload.models import Report


# Create your views here.
def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})

def seereport(request, report_id=None):
	print (report_id)
	if report_id == None:
		return render(request, 'ReportView.html', {'rep': 'no report here!'})
	return render_to_response('ReportView.html', {'report' : Report.objects.get(reportID=report_id)})