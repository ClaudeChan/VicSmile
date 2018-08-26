from django.shortcuts import render, HttpResponse

from django.db.models import Q

def index(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']

    return render(request, "search/index.html", ctx)
