from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    isActive=False
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is not None: isActive=True


    date = datetime.datetime.now()
    
    name="Ashhar"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime numbers',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Shad",
        'student_college':"GEC,Bhojpur",
        'student_city':"Biharsharif"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    print("home fuction is called from view")
    #return HttpResponse("<h1>Hello this is index page<h1>"+"<h3>{}<h3>".format(date))
    return render(request,"home.html",data)
def about(request):
    #return HttpResponse("<h1>This is about page<h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1>This is service page<h1>")
    return render(request,"services.html",{})