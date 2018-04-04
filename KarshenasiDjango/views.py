from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate,login,logout
from KarshenasiDjango.models import Professor,Project,Student,User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import recaptcha2


def indexpage(request):
    if User.is_authenticated :
        prjs = []
        if request.user.is_staff and request.user.is_superuser :
            prjs = []
            list = Project.objects.all()
            for x in list:
                prjs.append(x)
        elif request.user.is_staff :
            prjs = []
            list = Project.objects.filter(Professor_id=User.Professor.id)
            for x in list:
                prjs.append(x)
        else:
            prjs.append(Project.objects.get(StudentNumber = request.user.Student.StudentNumber))
        return render(request, "Dashboard.html", {'Data' : prjs })
    else:
        return HttpResponseRedirect('/Login')

def loginpage(request):
    return render(request, "Login.html", {})


def registerpage(request):
    return render(request, "Register.html", {})


def addprjpage(request):
    if User.is_authenticated :
        prfs = []
        list = User.objects.all().filter(is_staff=True)
        for x in list:
            prfs.append(x)

        return render(request, "AddProject.html", {'Data' : prfs})
    else:
        return HttpResponseRedirect('/Login')


def addprfpage(request) :
    if User.is_authenticated :
        prfs = []
        list = User.objects.all().filter(is_staff=True)
        for x in list :
            prfs.append(x)

        return render(request,"AddProfessor.html",{'Data' : prfs})
    else:
        return HttpResponseRedirect('/Login')


def findgroup(value) :
    if value == '10' :
        return "گروه شبکه های کامپیوتری و امنیت"
    elif value == '20' :
        return "گروه فناوری اطلاعات"
    elif value == '30' :
        return "گروه معماری سامانه های کامپیوتری"
    elif value == '40' :
        return "گروه نرم افزار و سیستم های اطلاعاتی"
    elif value == '50' :
        return "گروه هوش مصنوعی ، رباتیک ، رایانش"
    else :
        return "گروه ثبت نشده"


def addprofessor(request):
    if User.is_authenticated :
        if request.method == "POST":
            try :
              newprf = Professor()
              newprf.Group = findgroup(request.POST['Group'])
              newprf.MobilePhone = request.POST['MobilePhone']
              newprf.FullName = request.POST['FullName']
              newprf.save()
              newusr = User()

              newusr.password = make_password(request.POST['MobilePhone'])
              newusr.username = request.POST['Email']
              newusr.email = request.POST['Email']
              newusr.is_staff = True
              newusr.is_superuser = False
              newusr.Professor_id = newprf.id
              newusr.save()
              return HttpResponse("Success")
            except :
              return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')

def editprofessor(request):
    if User.is_authenticated :
        if request.method == "POST":
            try :
              changeusr = User.objects.get(id=request.POST['Id'])
              changeusr.set_password(request.POST['Password'])
              changeusr.username = request.POST['Username']
              changeusr.email = request.POST['Email']
              changeusr.save()
              changeprf = Professor.objects.get(id=changeusr.Professor_id)
              changeprf.Group = findgroup(request.POST['Group'])
              changeprf.MobilePhone = request.POST['MobilePhone']
              changeprf.FullName = request.POST['FullName']
              changeprf.save()
              return HttpResponse("Success")
            except :
              return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')






def delprofessor(request):
    if User.is_authenticated :
        if request.method == "POST":
            try:
                Professor.objects.filter(id=request.POST['Id']).delete()
                User.objects.filter(Professor=request.POST['Id']).delete()
                return HttpResponse("Success")
            except:
                return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')


def addproject(request):
    if User.is_authenticated :
        if request.method == "POST":
            try :
              newprj = Project()
              newprj.Title = request.POST['Title']
              newprj.StudentNumber = int(92213150)
              newprj.Professor_id = request.POST['Professor']
              newprj.Detail = request.POST['Detail']
              newprj.Requirements = request.POST['Requirements']
              newprj.TagofProject = request.POST['TagofProject']
              newprj.status = 1
              newprj.save()
              return HttpResponse("Success")
            except :
                return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')

def delproject(request):
    if User.is_authenticated :
        if request.method == "POST":
            try:
                return HttpResponse("Success")
            except:
                return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')



def acceptprj(request):
    if User.is_authenticated :
        if request.method == "POST":
            try:
                Change = Project.objects.get(id=request.POST['Id'])
                Change.status = Change.status+1
                Change.save()
                return HttpResponse("Success")
            except:
                return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')



def register(request):
    if request.method == "POST":
        try:
            Change = Project.objects.get(id=request.POST['Id'])
            Change.status = Change.status+1
            Change.save()
            return HttpResponse("Success")
        except:
            return HttpResponse("Error")
    else:
        return HttpResponse("Error")



def logins(request):
    if request.method == "POST":
        try:
            Captcha = recaptcha2.verify('6LeVPlAUAAAAAAcPf_pai8VCdA37urPVZTeX91z_', request.POST['g-recaptcha-response'], '127.0.0.1')
            if Captcha['success'] == True:
                Mahdi = authenticate(username=request.POST['username'],password=request.POST['password'])
                if Mahdi is not None :
                        login(request,Mahdi)
                        return HttpResponseRedirect('/Dashboard')
                else:
                    return render(request, "Login.html", {'error' : ' نام کاربری یا پسورد اشتباه وارد شده است'})
            else:
                return render(request, "Login.html", {'error': 'مشکل در چک کننده ربات (Recaptcha)'})
        except:
            return render(request, "Login.html", {'error': 'با پشتیبانی پرتال تماس بگیرید'})
    else:
        return render(request, "Login.html", {'error': 'مجددا تلاش کنید'})


def Registers(request):
    if request.method == "POST":
        try:
            Captcha = recaptcha2.verify('6LeVPlAUAAAAAAcPf_pai8VCdA37urPVZTeX91z_', request.POST['g-recaptcha-response'], '127.0.0.1')
            if Captcha['success'] == True:
                newstd = Student()
                newstd.StudentField = request.POST['field']
                newstd.StudentNumber = request.POST['studentnumber']
                newstd.FullName = request.POST['fullname']
                newstd.MobilePhone = request.POST['mobilephone']
                if (newstd.StudentField == 0) :
                    newstd.StudentPrf_id = 1
                else:
                    newstd.StudentPrf_id = 2

                newstd.save()
                User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'],Student_id= newstd.id)
                Mahdi = authenticate(username=request.POST['username'],password=request.POST['password'])
                if Mahdi is not None :
                        login(request,Mahdi)
                        return HttpResponseRedirect('/Dashboard')
                else:
                    return render(request, "Register.html", {'error' : ' نام کاربری یا پسورد اشتباه وارد شده است'})
            else:
                return render(request, "Register.html", {'error': 'مشکل در چک کننده ربات (Recaptcha)'})
        except:
            return render(request, "Register.html", {'error': 'تمامی فیلد ها باید به درستی پر شوند . با پشتیبانی تماس بگیرید'})
    else:
        return render(request, "Register.html", {'error': 'مجددا تلاش کنید'})

def logouts(request):
        try:
            logout(request)
            return HttpResponseRedirect('/Login')
        except:
            return HttpResponse("Error")

