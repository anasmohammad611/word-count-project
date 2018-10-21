from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')


def count(request):
    ft= request.GET['fulltext']
    wl = ft.split()
    wd = {}
    for word in wl:
        if word in wd:
            wd[word]+=1
        else:
            wd[word]=1

    sw = sorted(wd.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'fulltext':ft,'count':len(wl),'wd':sw})

def about(request):
    return render(request,'about.html')
