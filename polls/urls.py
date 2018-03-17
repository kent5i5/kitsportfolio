'''
Created on Aug 29, 2017

@author: kenng
'''
#from django.conf.urls import url
app_name = 'polls'
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
        # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]