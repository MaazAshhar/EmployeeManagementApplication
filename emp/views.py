from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Testimonial,Feedback
from .forms import FeedbackForm

# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method=='POST':
        # Fetch data
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_working=request.POST.get("emp_working")
        emp_address=request.POST.get("emp_address")
        emp_department=request.POST.get("emp_department")

        # Create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        # Save the data
        e.save()

        # Prepare msg

        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})


def delete_emp(request,emp_id):
    print(emp_id)
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_address=request.POST.get("emp_address")
        emp_department=request.POST.get("emp_department")
        emp_working= request.POST.get("emp_working")
        emp_phone=request.POST.get("emp_phone")

        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        
        e.save()


    return redirect("/emp/home/")


def testimonial(request):
    testi=Testimonial.objects.all()
    return render(request,"emp/testimonials.html",{'testi':testi})


def add_feedback(request):
    form=FeedbackForm()
    return render(request,"emp/add_feedback.html",{'form':form})


def view_feedback(request):
    bool=False
    if request.method=="POST":
        f=FeedbackForm(request.POST)
        if f.is_valid():
            new_feedback=f.save()
            bool=True
        feedbacks=Feedback.objects.all()
        data={'bool':bool,'feedbacks':feedbacks}
        return render(request,"emp/view_feedback.html",data)
    feedbacks=Feedback.objects.all()
    if(len(feedbacks)!=0):
        bool=True
    data={'bool':bool,'feedbacks':feedbacks}
    return render(request,"emp/view_feedback.html",data)