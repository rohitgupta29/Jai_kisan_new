from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html" )

def result(request):
    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['Region'])
    lis.append(request.GET['Sowing Time'])
    lis.append(request.GET['pH'])
    lis.append(request.GET['Soil Type'])

    print (lis)

    ans = cls.predict([lis])

    return render(request,"result.html",{'ans':ans, 'lis': lis})