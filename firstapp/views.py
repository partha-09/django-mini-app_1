from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Details,Registration
# Create your views here.
def fun(request):
    return HttpResponse("<h1>Hello from Djoango<h1>") ;
def message(request):
    return HttpResponse("Well come message....!");
def home(request):
    if request.method=="POST":
        firstname=request.POST.get('name')
        home=Details(firstname=firstname)
        home.save()
    return render(request,"home.html");
# def contact(request):
#     namelist=Details.objects.all()
#     return HttpResponse(namelist) #displays all the values of rows in a single line not stylied
def contact(request):
    namelist=Details.objects.all()
    context={
        'namelist':namelist,
    }
    return render(request,'Inquiry.html',context)
