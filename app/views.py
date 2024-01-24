from django.http import HttpResponse
from django.shortcuts import render

def homeview(request):
    print(str(request))
    return render (request=request, template_name='index.html', context={})

def messageview(request):
    return HttpResponse ("Mu home view edi")