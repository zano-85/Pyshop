from django.http import HttpResponse
from django.shortcuts import render


def index1(request):
    return HttpResponse('Hellow in post view')


def new_post(request):
    return HttpResponse('new post')
