from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate,login,logout
from KarshenasiDjango.models import Professor,Project,Student,User
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import recaptcha2


def indexpage(request):
    if User.is_authenticated :
        prjs1 = []
        prjs = []
        prfs = []
        if request.user.is_staff and request.user.is_superuser :
            try:
                list = Project.objects.all()
                for x in list:
                    prjs.append(x)

                list2 = User.objects.all().filter(is_staff=True)
                for x in list2:
                    prfs.append(x)
            except:
                prjs = None
                prfs = None

        elif request.user.is_staff :
            try:
                listref1 = Project.objects.filter(referee1_id =request.user.Professor.id)
                listref2 = Project.objects.filter(referee2_id =request.user.Professor.id)
                list = Project.objects.filter(Professor_id=request.user.Professor.id)
                for x in list:
                    prjs.append(x)

                for x in listref1 :
                    prjs1.append(x)

                for x in listref2 :
                    prjs1.append(x)
            except:
                prjs = None
                prfs = None
        else:
            try:
                prjs.append(Project.objects.get(Student_id = request.user.Student.id))
            except:
                prjs  = None
                prfs = None

        return render(request, "Dashboard.html", {'Data' : prjs , 'Data2' : prfs , 'Data3' : prjs1 })
    else:
        return HttpResponseRedirect('/Login')

def loginpage(request):
    return render(request, "Login.html", {})


def registerpage(request):
    return render(request, "Register.html", {})


def detailproject(request) :
    prj = Project.objects.get(id=request.GET['Id'])
    if request.user.is_staff == 0 :
        if prjid.Student_id == request.user.Student_id :
            return render(request, "DetailProject.html", {'Data': prj})
        else:
            return render(request, "Dashboard.html")
    else:
        return render(request, "DetailProject.html", {'Data': prj})


    return render(request , "")

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

              newusr.set_password(request.POST['MobilePhone'])
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
                Test = Project.objects.filter(Student_id=request.user.Student.id).count()
                if Test == 1 :
                    return HttpResponse("Error2")
                else:
                    newprj = Project()
                    newprj.Title = request.POST['Title']
                    newprj.Student_id = request.user.Student_id
                    newprj.StudentNumber = request.user.Student.StudentNumber
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



def deadline(request):
    if User.is_authenticated :
        if request.method == "POST":
            try:
                Change = Project.objects.get(id=request.POST['Id'])
                Change.DeadlineDate = request.POST['DeadlineDate']
                Change.DeadlineTime = request.POST['DeadlineTime']
                Change.referee1_id = request.POST['referee1']
                Change.referee2_id = request.POST['referee2']
                Change.save()
                return HttpResponse("Success")
            except:
                return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')

def score(request):
    if User.is_authenticated :
        if request.method == "POST":
            try:
                Change = Project.objects.get(id=request.POST['Id'])
                if Change.Professor_id == request.user.Professor_id:
                    Change.Professor_Score = request.POST['Score']
                elif Change.referee1_id == request.user.Professor_id:
                    Change.referee1_Score = request.POST['Score']
                elif Change.referee2_id == request.user.Professor_id:
                    Change.referee2_Score = request.POST['Score']

                Change.save()
                return HttpResponse("Success")
            except:
                return HttpResponse("Error")
        else:
            return HttpResponse("Error")
    else:
        return HttpResponseRedirect('/Login')


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



def FirstUploadPresentFile(request):
    if request.method == 'POST' and request.FILES['mypresentfile']:
        try:
            prj = Project.objects.get(Student_id=request.user.Student.id)

            myfile = request.FILES['mypresentfile']
            fs = FileSystemStorage()
            FileName = "[" + str(request.user.Student.StudentNumber) + "]" + "[PresentFile].pdf"
            prj.PresentFile = FileName
            prj.status = prj.status + 1
            prj.save()
            filename = fs.save(FileName, myfile)
            return HttpResponseRedirect('/Dashboard')
        except:
            return HttpResponseRedirect('/Dashboard')
    else:
        return HttpResponseRedirect('/Dashboard')

def EditUploadedPresentFile(request):
    if request.method == 'POST' and request.FILES['mypresentfile']:
        try:
            prj = Project.objects.get(Student_id=request.user.Student.id)

            myfile = request.FILES['mypresentfile']
            fs = FileSystemStorage()
            FileName = "[" + str(request.user.Student.StudentNumber) + "]" + "[PresentFile].pdf"
            prj.PresentFile = FileName
            prj.save()
            filename = fs.save(FileName, myfile)
            return HttpResponseRedirect('/Dashboard')
        except:
            return HttpResponseRedirect('/Dashboard')
    else:
        return HttpResponseRedirect('/Dashboard')

def FirstUploadProjectFile(request):
    if request.method == 'POST' and request.FILES['myprojectfile']:
        try:
            prj = Project.objects.get(Student_id=request.user.Student.id)

            myfile = request.FILES['myprojectfile']
            fs = FileSystemStorage()
            FileName = "[" + str(request.user.Student.StudentNumber) + "]" + "[ProjectFile].zip"
            prj.ProjectFile = FileName
            prj.status = prj.status + 1
            prj.save()
            filename = fs.save(FileName, myfile)
            return HttpResponseRedirect('/Dashboard')
        except:
            return HttpResponseRedirect('/Dashboard')
    else:
        return HttpResponseRedirect('/Dashboard')



def EditUploadedProjectFile(request):
    if request.method == 'POST' and request.FILES['myprojectfile']:
        try:
            prj = Project.objects.get(Student_id=request.user.Student.id)

            myfile = request.FILES['myprojectfile']
            fs = FileSystemStorage()
            FileName = "[" + str(request.user.Student.StudentNumber) + "]" + "[ProjectFile].zip"
            prj.ProjectFile = FileName
            prj.save()
            filename = fs.save(FileName, myfile)
            return HttpResponseRedirect('/Dashboard')
        except:
            return HttpResponseRedirect('/Dashboard')
    else:
        return HttpResponseRedirect('/Dashboard')
