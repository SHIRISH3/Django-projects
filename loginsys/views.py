from django.shortcuts import render
from loginsys.models import Newuser
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request,'index.html')


def userreg(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['pwd']
        age=request.POST['age']
        gender=request.POST['gender']
        maritialstatus=request.POST['maritialstatus']
        Newuser(username=username,email=email,pwd=pwd,age=age,gender=gender,maritialstatus=maritialstatus).save()
        messages.success(request,'New User'+request.POST['username']+"is saved successfully")
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def loginpage(request):
    if request.method=="POST":
        try:
            userdetails=Newuser.objects.get(email=request.POST['email'],pwd= request.POST['pwd'])
            print("username=",userdetails)
            request.session['email']=userdetails.email
            return render(request,'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'username/ pass invalid')
        return render(request,'login.html')