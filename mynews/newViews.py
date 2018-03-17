# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
#from botocore.vendored.requests.api import request

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<dr>Hello world</dr>")

def detail(request, article_id):
    return HttpResponse("You're looking at question %s." % article_id)

def update(request, article_id):
    response = "You updated article %s."
    return HttpResponse(response % article_id)

#def vote(request, article_id):
    #return HttpResponse("You're voting on question %s." % article_id)