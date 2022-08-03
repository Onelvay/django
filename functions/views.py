from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Internship,Body,Applicants
 

def home(request):
    inters = Body.objects.all()
    return render(request, "home.html", {"inters": inters})
 

def Create_Post(request):
    if request.method == "POST":

        name=request.POST.get("name")
        data=request.POST.get("data")
        info = request.POST.get("info")
        link=request.POST.get("link")

        inter=Internship.objects.create(name=name)
        inter.body_set.create(deadline=data, information=info,link=link)
        inter.save()
        # return HttpResponseRedirect("/success")
        return render(request,"success.html")
    return render(request,"AddPost.html")

# def success(request):
#     return render(request,"success.html")

def registration(request):
    if request.method == "POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        company=request.POST.get("way")
        
        internship=Internship.objects.get(name=company)      
        internship.applicants_set.create(first_name=fname,last_name=lname)
        return render(request, "success.html")
    inters=Body.objects.all()
    return render ( request, "registration.html", {"inters":inters})
