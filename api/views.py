from django.shortcuts import render
from django.http import HttpResponse
from .tasks import task2

def index(request):
    task2.delay()
    return HttpResponse('<h3>Celery!</h3>')