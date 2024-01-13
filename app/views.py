from django.shortcuts import render

# Create your views here.


def filter(request):
     d={'data':'who are You'}
     return render(request,'userfilter.html',d)