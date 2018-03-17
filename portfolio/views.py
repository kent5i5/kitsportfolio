from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    title = "Kitsportfolio"
    #context = {'title': title,}
    return render(request, 'portfolio/index.html', {'title': title})
