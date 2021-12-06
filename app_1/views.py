from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('key\ninfo')
    return render(request, 'app_1/index.html', {})
