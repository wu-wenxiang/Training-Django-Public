import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'time.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)