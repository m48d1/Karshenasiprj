from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'Dashboard/AddProject/Add', views.addproject, name="AddProject"),
    url(r'Dashboard/AddProfessor/Add', views.addprofessor, name="AddProfessor"),
    url(r'Dashboard/AddProject', views.addprjpage , name="AddProjectPage"),
    url(r'Dashboard/AddProfessor', views.addprfpage, name="AddProfessorPage"),
    url(r'Dashboard/DelProfessor', views.delprofessor, name="DeleteProfessor"),
    url(r'Dashboard/EditProfessor', views.editprofessor, name="EditProfessor"),
    url(r'Dashboard/DelProject', views.delproject, name="DeleteProject"),
    url(r'Dashboard/AcceptProject', views.acceptprj, name="AcceptProject"),
    url(r'RegisterForm', views.Registers, name="RegisterForm"),
    url(r'Register', views.registerpage, name="RegisterPage"),
    url(r'LoginForm', views.logins, name="LoginForm"),
    url(r'Login', views.loginpage, name="LoginPage"),
    url(r'Logout', views.logouts, name="Logout"),

    # url(r'^dashboard/user/'$, views.user , name="user"),
    url(r'Dashboard', views.indexpage, name="index"),
    url(r'', views.loginpage, name="index"),
        ]