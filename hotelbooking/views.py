from django.shortcuts import render
from .models import Room
from .models import Check_Availability
from .models import UserRegister
from .models import Contact


# Create your views here.
def openHomePage(request):
    type="home"
    return render(request,"index.html",{"type":type})
def openUserLogin(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openUserRegister(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openServicesPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openContactPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openCancelPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openCheck_Availability(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
#==================================================================================
def registerUser(request):
    u_fname=request.POST.get('u_fname')
    u_lname=request.POST.get('u_lname')
    u_email=request.POST.get('u_email')
    u_pass=request.POST.get('u_pass')
    u_rpass=request.POST.get('u_rpass')
    u_cno=request.POST.get('u_cno')
    u_add=request.POST.get('u_add')
    print(u_fname,u_lname,u_email,u_pass,u_pass,u_rpass,u_cno,u_add)
    ur=UserRegister(fname=u_fname,lname=u_lname,email_id=u_email,password=u_pass,rpassword=u_rpass,contact_no=u_cno,address=u_add)
    ur.save()
    return render(request,"index.html",{"type":'h_user',"message":'User Register Successfully'})
def loginUser(request):
    username=request.POST.get('email')
    password=request.POST.get('pass')
    res=UserRegister.objects.filter(email_id=username,password=password)

    if not res:
        return render(request,'index.html',{"type":'h_user',"message":'Invalid'})
    else:
        for x in res:
            print(x)

        return render(request,'index2.html',{"type":'type',"name":x})

#======================================================================================================
def ContactPage(request):
    print("57u7676")
    u_name=request.POST.get('u_name')
    u_email=request.POST.get('u_email')
    u_phone=request.POST.get('u_phone')
    u_mess=request.POST.get('u_mess')
    print(u_name,u_email,u_phone,u_phone,u_mess)
    uc=Contact(name=u_name,Email_id=u_email,phone_no=u_phone,message=u_mess)
    uc.save()
    print(uc)
    return render(request,'index.html',{"type":'h_contact',"message":'Successfully message sent'})
