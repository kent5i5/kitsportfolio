'''
Created on Sep 15, 2017

@author: kenng
'''

from django.conf.urls import url

from . import newViews

urlpatterns = [
    url(r'$', newViews.index, name='index')
]