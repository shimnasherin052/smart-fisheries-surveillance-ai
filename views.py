import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create ydefour views here.
from Fisheries import settings
from myapp.models import *


def login_get(request):
    # return render(request,"login.html")
    return render(request,"new_login.html")


def login_post(request):
    username=request.POST['username']
    password=request.POST['password']

    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        if user.groups.filter(name='admin').exists():
            return redirect('/myapp/adminhome/')
        elif user.groups.filter(name='Authority').exists():
            return redirect('/myapp/authority_index_get/')
        else:
            return redirect('/myapp/login_get')
    else:
        return redirect('/myapp/login_get')



def forgot_passwordget(request):
    return render(request,"forgot password.html")

def forgot_passwordpost(request):
    email=request.POST['email']
    return  redirect('/myapp/change_passwordget')

# --------------- A D M I N-------------

@login_required(login_url="/myapp/login_get/")
def adminhome(request):
    return render(request,'admin pages/admin index.html')


@login_required(login_url="/myapp/login_get/")
def authority_get(request):
    return render(request,"admin pages/add authority.html")

@login_required(login_url="/myapp/login_get/")
def authority_post(request):
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    pincode=request.POST['pincode']
    post=request.POST['post']
    city=request.POST['city']

    user=User.objects.create_user(username=email,password=phone)
    user.groups.add(Group.objects.get(name='Authority'))
    user.save()

    obj=Authority()
    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.place=place
    obj.pin=pincode
    obj.post=post
    obj.city=city
    obj.AUTHUSER=user
    obj.save()

    return redirect('/myapp/viewauthority_get/')

@login_required(login_url="/myapp/login_get/")
def editauthority_get(request,id):
    data=Authority.objects.get(id=id)
    return render(request, "admin pages/edit authority.html",{'data':data})

@login_required(login_url="/myapp/login_get/")
def editauthority_post(request):
    name=request.POST['name']
    email=request.POST['email']
    phoneno=request.POST['phoneno']
    place=request.POST['place']
    pincode=request.POST['pincode']
    post=request.POST['post']
    city=request.POST['city']
    id=request.POST['id']

    obj=Authority.objects.get(id=id)

    # user=obj.AUTHUSER
    # user.username=email
    # user.save()

    obj.name=name
    obj.email=email
    obj.phone=phoneno
    obj.place=place
    obj.pin=pincode
    obj.post=post
    obj.city=city
    obj.save()

    return redirect('/myapp/viewauthority_get/#a')

@login_required(login_url="/myapp/login_get/")
def deleteauthority_get(request,id):
    Authority.objects.get(id=id).delete()
    User.objects.get(id=id)

    return redirect('/myapp/viewauthority_get')

@login_required(login_url="/myapp/login_get/")
def addnotification_get(request):
    return render(request, "admin pages/add notification.html")


@login_required(login_url="/myapp/login_get/")
def addnotification_post(request):
    nootification=request.POST['Notification']

    obj=Notification()
    obj.notification=nootification
    obj.date=datetime.datetime.now().today()
    obj.save()
    return redirect('/myapp/viewnotification_get/')

@login_required(login_url="/myapp/login_get/")
def viewnotification_get(request):
    a=Notification.objects.all()
    return render(request,"admin pages/view notification.html",{'data':a})

#
# def editnotification_get(request,id):
#     a=Notification.objects.get(id=id)
#     return render(request, "admin pages/add notification.html",{'data':a})
#
# def editnotification_post(request):
#     id=request.POST['id']
#     Notification=request.POST['Notification']
#
#     obj=Notification.objects.get(id=id)
#     obj.notification=Notification
#     obj.date=datetime.datetime.now().today()
#     obj.save()
#     return redirect('/myapp/viewnotification_get/')


@login_required(login_url="/myapp/login_get/")
def deletenotification_get(request,id):
    Notification.objects.get(id=id).delete()
    return redirect('/myapp/viewnotification_get/')









@login_required(login_url="/myapp/login_get/")
def add_rescueteam_get(request):
    return render(request,"admin pages/add rescue team.html")

@login_required(login_url="/myapp/login_get/")
def add_rescueteam_post(request):
    name =request.POST['name']
    email=request.POST['email']
    place=request.POST['place']
    phoneno=request.POST['phoneno']
    photo=request.FILES['photo']

    user = User.objects.create_user(username=email, password=phoneno)
    user.groups.add(Group.objects.get(name='Rescueteam'))
    user.save()

    fs=FileSystemStorage()
    date=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
    fs.save(date,photo)
    path=fs.url(date)

    obj=Rescue()
    obj.name=name
    obj.email=email
    obj.phone=phoneno
    obj.place=place
    obj.photo=path
    obj.AUTHUSER=user
    obj.save()
    return redirect('/myapp/viewrescue_get/')


@login_required(login_url="/myapp/login_get/")
def viewrescue_get(request):
    data=Rescue.objects.all()
    return render(request,"admin pages/view rescue team.html",{'data':data})

@login_required(login_url="/myapp/login_get/")
def delete_rescue(request,id):
    Rescue.objects.get(id=id).delete()
    return redirect('/myapp/viewrescue_get/')




@login_required(login_url="/myapp/login_get/")
def editrescueteam_get(request,id):
    data=Rescue.objects.get(id=id)
    return render(request,"admin pages/edit rescue team.html",{'data':data})

@login_required(login_url="/myapp/login_get/")
def editrescueteam_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    place = request.POST['place']
    id= request.POST['id']
    obj = Rescue.objects.get(id=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path
        obj.save()

    obj.name = name
    obj.email = email
    obj.phone = phoneno
    obj.place = place
    obj.save()
    return redirect('/myapp/viewrescue_get/#a')

@login_required(login_url="/myapp/login_get/")
def viewalert_get(request):
    a=Alert.objects.all().order_by('-id')
    return render(request,"admin pages/view alert.html",{'data':a})

@login_required(login_url="/myapp/login_get/")
def viewauthority_get(request):
    data=Authority.objects.all()
    return render(request,"admin pages/view authority.html",{'data':data})

@login_required(login_url="/myapp/login_get/")
def viewrescueteam_get(request):
    return render(request,"admin pages/view rescue team.html")

@login_required(login_url="/myapp/login_get/")
def viewuser_get(request):
    a=Users.objects.all()
    print(a,"user details")
    return render(request,"admin pages/viewuser.html",{'data':a})


@login_required(login_url="/myapp/login_get/")
def viewcomplaint_get(request):
    a=Complaint.objects.all()
    return render(request,"admin pages/view complaint.html",{'data':a})


@login_required(login_url="/myapp/login_get/")
def sendreply_get(request,id):
    return render(request,"admin pages/sentreply.html",{'id':id})


@login_required(login_url="/myapp/login_get/")
def sendreply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']

    obj=Complaint.objects.get(id=id)
    obj.date=datetime.datetime.now().today()
    obj.status="replied"
    obj.reply=reply
    obj.save()

    return redirect('/myapp/viewcomplaint_get/')



@login_required(login_url="/myapp/login_get/")
def change_password_get(request):
    return render(request,'admin pages/change password.html')

@login_required(login_url="/myapp/login_get/")
def change_password_post(request):
    currentpassword=request.POST['oldpassword']
    newpassword=request.POST['currentpassword']
    confirmpassword=request.POST['confirmpassword']
    data=request.user
    if data.check_password(currentpassword):
        if newpassword==confirmpassword:
            data.set_password(newpassword)
            data.save()
            return redirect('/myapp/login_get/')
        else:
            return render(request,'admin pages/change password.html')
    else:
        return render(request,'admin pages/change password.html')


def loginpage_get(request):
    logout(request)
    return redirect('/myapp/login_get/')


#authority




@login_required(login_url="/myapp/login_get/")
def auth_change_password_get(request):
    return render(request,'change password.html')

@login_required(login_url="/myapp/login_get/")
def auth_change_password_post(request):
    currentpassword=request.POST['oldpassword']
    newpassword=request.POST['currentpassword']
    confirmpassword=request.POST['confirmpassword']
    data=request.user
    if data.check_password(currentpassword):
        if newpassword==confirmpassword:
            data.set_password(newpassword)
            data.save()
            return redirect('/myapp/login_get/')
        else:
            return redirect('/myapp/auth_change_password_get/#a')
    else:
        return redirect('/myapp/auth_change_password_get/#a')


def authority_index_get(request):
    return render(request,'authority pages/authority index.html')



def authority_addzone_get(request):
    return render(request,'authority pages/add zone.html')

def authority_addzone_post(request):
    latitude=request.POST['latitude']
    longitude=request.POST['longitude']

    obj=Zone()
    obj.latitude=latitude
    obj.longitude=longitude
    obj.date=datetime.datetime.today()
    obj.status='pending'
    obj.AUTHORITY=Authority.objects.get(AUTHUSER=request.user)
    obj.save()
    return redirect('/myapp/authority_viewzone_get/')

def authority_editzone_get(request,id):
    data=Zone.objects.get(id=id)
    return render(request,'authority pages/edit zone.html',{'data':data})

def authority_editzone_post(request):
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    id= request.POST['id']

    obj = Zone.objects.get(id=id)
    obj.latitude = latitude
    obj.longitude = longitude
    obj.date = datetime.datetime.today()
    obj.save()
    return redirect('/myapp/authority_viewzone_get/')


def authority_viewzone_get(request):
    data=Zone.objects.filter(AUTHORITY__AUTHUSER=request.user)
    return render(request,'authority pages/view zone.html',{'data':data})

def authority_delete_zone(request,id):
    Zone.objects.filter(id=id).delete()
    return redirect('/myapp/authority_viewzone_get/')

def authority_addbanschedule_get(request):
    z=Zone.objects.filter(AUTHORITY__AUTHUSER=request.user)
    return render(request,'authority pages/add banschedule.html',{'z':z})

def authority_addbanschedule_post(request):
    zone=request.POST['zone']
    fromdate=request.POST['from']
    to=request.POST['to']

    obj=Banschedule()
    obj.ZONE_id=zone
    obj.from_date=fromdate
    obj.to_date=to
    obj.status='Banned'
    obj.save()

    obj1=Zone.objects.get(id=zone)
    obj1.status='Banned'
    obj1.save()
    return redirect('/myapp/authority_viewbanschedule/')


def authority_editbanschedule_get(request,id):
    z=Zone.objects.filter(AUTHORITY__AUTHUSER=request.user)
    data=Banschedule.objects.get(id=id)
    return render(request,'authority pages/edit banschedule.html',{'z':z,'data':data})

def authority_editbanschedule_post(request):
    zone=request.POST['zone']
    fromdate=request.POST['from']
    status=request.POST['status']
    to=request.POST['to']
    id=request.POST['id']
    obj = Banschedule.objects.get(id=id)
    obj.ZONE_id = zone
    obj.from_date = fromdate
    obj.to_date = to
    obj.status = status
    obj.save()
    return redirect('/myapp/authority_viewbanschedule/#a')
def authority_viewbanschedule(request):
    data=Banschedule.objects.filter(ZONE__AUTHORITY__AUTHUSER=request.user)
    return render(request,'authority pages/view banschedule.html',{'data':data})

def banschedule_delete(request,id):
    Banschedule.objects.filter(id=id).delete()
    return redirect('/myapp/authority_viewbanschedule/')


def authority_viewalert_get(request):
    data=Alert.objects.all().order_by('-id')
    return render(request,'authority pages/view alert.html',{'data':data})



def authority_viewhelprequest_get(request):
    data=Help.objects.all().order_by('-id')
    return render(request,'authority pages/view help request.html',{'data':data})

def authority_viewnotification_get(request):
    data=Notification.objects.all().order_by('-id')
    return render(request,'authority pages/view notification.html',{'data':data})


def authority_viewprofile_get(request):
    data=Authority.objects.get(AUTHUSER=request.user)
    return render(request,'authority pages/view profile.html',{'data':data})


def authority_viewrescueteam_get(request):
    data=Rescue.objects.all()
    return render(request,'authority pages/view rescue team.html',{'data':data})


def authority_addboat_ownersget(request):
    return render(request,'authority pages/add boat owners.html')

def authority_addboat_owners(request):
    ownername=request.POST["name"]
    ownernumber=request.POST["ownernumber"]
    owneremail=request.POST["email"]
    ownerplace=request.POST["ownerplace"]
    boatregistrationid=request.POST["boatregistrationidost"]
    boatphoto=request.FILES["boatphoto"]
    proof=request.FILES["boatlicensephoto"]


    fs1=FileSystemStorage()
    date1=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'pic.jpg'
    fs1.save(date1,boatphoto)
    path1=fs1.url(date1)

    fs2 = FileSystemStorage()
    date2 = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + 'prf.jpg'
    fs2.save(date2, proof)
    path2 = fs2.url(date2)

    print(request.user.id,"ffffffff")

    c=Authority.objects.get(AUTHUSER_id=request.user.id).id
    print(c)

    obj=BoatRegister()
    obj.ownername=ownername
    obj.owneremail=owneremail
    obj.ownernumber=ownernumber
    obj.ownerplace=ownerplace
    obj.boatregistrationid=boatregistrationid
    obj.boatphoto=path1
    obj.boatlicensephoto=path2
    obj.AUTHORITY_id=c
    obj.save()
    return redirect('/myapp/authority_viewboatowners/')

def authority_viewboatowners(request):
    a=BoatRegister.objects.filter(AUTHORITY__AUTHUSER_id=request.user.id)
    return render(request,'authority pages/view boat owners.html',{'data':a})

def authority_editboat_ownersget(request,id):
    data=BoatRegister.objects.get(id=id)
    return render(request,'authority pages/edit boat owners.html',{'data':data})

def authority_editboat_owners(request):
    ownername=request.POST["name"]
    ownernumber=request.POST["ownernumber"]
    owneremail=request.POST["email"]
    ownerplace=request.POST["ownerplace"]
    boatregistrationid=request.POST["boatregistrationidost"]


    id=request.POST['id']

    obj = BoatRegister.objects.get(id=id)


    if 'boatphoto' in request.FILES:
        boatphoto = request.FILES["boatphoto"]
        fs1=FileSystemStorage()
        date1=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
        fs1.save(date1,boatphoto)
        path1=fs1.url(date1)
        obj.boatphoto = path1
        obj.save()



    if 'boatlicensephoto'in request.FILES:
        proof = request.FILES["boatlicensephoto"]
        fs2 = FileSystemStorage()
        date2 = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs2.save(date2, proof)
        path2 = fs2.url(date2)
        obj.boatlicensephoto=path2
        obj.save()


    print(request.user.id,"ffffffff")

    c=Authority.objects.get(AUTHUSER_id=request.user.id).id
    print(c)


    obj.ownername=ownername
    obj.owneremail=owneremail
    obj.ownernumber=ownernumber
    obj.ownerplace=ownerplace
    obj.boatregistrationid=boatregistrationid
    obj.save()
    return redirect('/myapp/authority_viewboatowners/')



@login_required(login_url="/myapp/login_get/")
def authority_viewnotification_get(request):
    a=Notification.objects.all().order_by('-id')
    return render(request,"authority pages/view notification.html",{'data':a})

@login_required(login_url="/myapp/login_get/")
def delete_boatowner(request,id):
    BoatRegister.objects.get(id=id).delete()
    return redirect('/myapp/authority_viewboatowners/')

# A N D R O I D ----------------------------------

def app_login(request):
    username=request.POST['Username']
    password=request.POST['Password']

    check=authenticate(request,username=username,password=password)

    if check is not None:
        login(request,check)
        if check.groups.filter(name='Users').exists():
            return JsonResponse({'status':'ok','lid':check.id,'type':'user'})
        elif check.groups.filter(name='Rescueteam').exists():
            return JsonResponse({'status':'ok','lid':check.id,'type':'rescue'})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status': 'no'})


#  U S E R S -------------------------------------------

def user_signup(request):
    name=request.POST['uname']
    email=request.POST['uemail']
    phoneno=request.POST['uphoneno']
    place=request.POST['uplace']
    pin=request.POST['upin']
    post=request.POST['upost']
    boat_id=request.POST['uboat_id']
    city=request.POST['ucity']
    password=request.POST['upassword']
    confirmpassword = request.POST['uconfirmpassword']
    photo=request.FILES['photo']

    user=User.objects.create_user(username=email,password=password)
    user.groups.add(Group.objects.get(name='Users'))
    user.save()

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
    fs.save(date, photo)
    path = fs.url(date)

    obj=Users()
    obj.name=name
    obj.email=email
    obj.number=phoneno
    obj.place=place
    obj.pin=pin
    obj.post=post
    obj.city=city
    obj.BOATREGISTER_id=boat_id
    obj.photo=path
    obj.AUTHUSER=user

    obj.save()

    return JsonResponse({'status':'ok'})



def user_viewprofile(request):
    lid=request.POST['lid']
    a=Users.objects.get(AUTHUSER=lid)
    return JsonResponse({'status':'ok',
                         'name':a.name,
                         'number':a.number,
                         'email':a.email,
                         'place':a.place,
                         'pin':a.pin,
                         'post':a.post,
                         'city':a.city,
                         'boatowner_name':a.BOATREGISTER.ownername,
                         'boat_id':a.BOATREGISTER.boatregistrationid,
                         'photo':a.photo,
                         })



def user_viewprofilehome_page(request):
    lid=request.POST['lid']
    a=Users.objects.get(AUTHUSER=lid)
    return JsonResponse({'status':'ok',
                         'name':a.name,
                         'photo':a.photo,
                         })





def user_editprofile(request):
    lid=request.POST['lid']
    name = request.POST['uname']
    phoneno = request.POST['uphoneno']
    place = request.POST['uplace']
    pin = request.POST['upin']
    post = request.POST['upost']
    city = request.POST['ucity']
    boat_id = request.POST['uboat_id']

    obj = Users.objects.get(AUTHUSER=lid)
    obj.name = name
    obj.number = phoneno
    obj.place = place
    obj.pin = pin
    obj.post = post
    obj.city = city
    obj.BOATREGISTER_id = boat_id

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.jpg'
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path
        obj.save()

    obj.save()

    return JsonResponse({'status':'ok'})



def user_viewzones(request):
    a=Zone.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'statuss':i.status,
                  'latitude':i.latitude,
                  'longitude':i.longitude,
                  'authority':i.AUTHORITY.name,
                  })
        print(l)
    return  JsonResponse({'status':'ok','data':l})


def user_viewbanschedule(request):
    zid=request.POST['zid']
    a=Banschedule.objects.filter(ZONE=zid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'from_date':i.from_date,
                  'to_date':i.to_date,
                  'statuss':i.status,
                  'latitude':i.ZONE.latitude,
                  'longitude':i.ZONE.longitude,
                  })
        print(l)
    return JsonResponse({'status': 'ok', 'data': l})

def user_viewalert(request):
    a=Alert.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'statuss':i.status,
                  'time':i.time,
                  'detection':i.detection,
                  })

        print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def user_viewrescueteam(request):
    a=Rescue.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({
            'id':i.id,
                  'name':i.name,
                  'phone':i.phone,
                  'email':i.email,
                  'place':i.place,
                  'photo':i.photo,

              })
        print(l)
    return JsonResponse({'status': 'ok', 'data': l})



def user_sendhelp_request(request):
    rid=request.POST['rid']
    lid=request.POST['lid']
    latitude = request.POST['ulatitude']
    longitude = request.POST['ulongitude']

    print(rid,lid,latitude,longitude)

    obj=Help()
    obj.date=datetime.datetime.now().date()
    obj.time=datetime.datetime.now()
    obj.status='pending'
    obj.latitude=latitude
    obj.longitude=longitude
    obj.RESCUETEAM=Rescue.objects.get(id=rid)
    obj.USERS=Users.objects.get(AUTHUSER_id=lid)
    obj.save()
    return JsonResponse({"status":"ok"})


def user_viewhelpStatus(request):
    lid=request.POST['lid']
    a=Help.objects.filter(USERS__AUTHUSER_id=lid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'time':i.time,
                  'statuss':i.status,
                  'latitude':i.latitude,
                  'longitude':i.longitude,
                  'name':i.RESCUETEAM.name,
                  'photo':i.RESCUETEAM.photo,

              })
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})




def userchange_password(request):
    lid=request.POST['lid']
    currentpassword=request.POST['currentpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    print(currentpassword,newpassword,confirmpassword)

    data=User.objects.get(id=lid)
    if data.check_password(currentpassword):
        if newpassword==confirmpassword:
            data.set_password(newpassword)
            data.save()
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status': 'not'})

    else:
        return  JsonResponse({'status':'not'})


def userviewnotification(request):
    a=Notification.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'notification':i.notification,
                  })
        print(l)
    return JsonResponse({'status':'ok', 'data':l})


# --------rescue------

def rescueviewprofile(request):
    lid = request.POST['lid']
    a = Rescue.objects.get(AUTHUSER=lid)
    return JsonResponse({'status': 'ok',
                         'name': a.name,
                         'phone': a.phone,
                         'email': a.email,
                         'place': a.place,
                         'photo': a.photo,
                         })




def rescueviewprofilehome_page(request):
    lid = request.POST['lid']
    a = Rescue.objects.get(AUTHUSER=lid)
    return JsonResponse({'status': 'ok',
                         'name': a.name,
                         'photo': a.photo,
                         })






def  rescue_viewzones(request):
    a=Zone.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'statuss':i.status,
                  'latitude':i.latitude,
                  'longitude':i.longitude,
                  'authority':i.AUTHORITY.name,
                  })
        print(l)
    return  JsonResponse({'status':'ok','data':l})


def rescue_viewbanschedule(request):
    zid=request.POST['zid']
    a=Banschedule.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'from_date':i.from_date,
                  'to_date':i.to_date,
                  'statuss':i.status,
                  'latitude':i.ZONE.latitude,
                  'longitude':i.ZONE.longitude,
                  })
        print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def rescue_viewalert(request):
    a=Alert.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'statuss':i.status,
                  'time':i.time,
                  'detection':i.detection,
                  })

    print(l)
    return JsonResponse({'status': 'ok', 'data': l})

def rescue_viewhelprequest(request):
    lid=request.POST['lid']
    a=Help.objects.filter(RESCUETEAM__AUTHUSER_id=lid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'time':i.time,
                  'statuss':i.status,
                  'latitude':i.latitude,
                  'longitude':i.longitude,
                  'name':i.USERS.name,
                  'photo':i.USERS.photo,

              })
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def rescueviewnotification(request):
    a=Notification.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'date':i.date,
                  'notification':i.notification,
                  })
    print(l)
    return JsonResponse({'status':'ok', 'data':l})



from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Help, Alert

def get_new_notifications(request):
    lid = request.POST.get('lid')
    now = timezone.now()
    time_limit = now - timedelta(minutes=2)

    new_help_requests = Help.objects.filter(
        RESCUETEAM__AUTHUSER=lid,
        status='pending',
        date=now.date(),
        # time__gte=time_limit.time()
    )

    new_alerts = Alert.objects.filter(
        status='ACTIVE',
        date=now.date(),
        # time__gte=time_limit.time()
    )

    notifications = []

    for help_req in new_help_requests:
        notifications.append({
            'type': 'help',
            'message': f'Help request from {help_req.USERS.name}',
        })

    for alert in new_alerts:
        notifications.append({
            'type': 'alert',
            'message': f'New alert: {alert.status}',
        })


    print(notifications)




    return JsonResponse({
        'status': 'ok',
        'notifications': notifications
    })

def rescue_update_all_alerts(request):
    Alert.objects.filter(status='ACTIVE').update(status='SEEN')
    return JsonResponse({"status": "ok"})


def fetchcount(request):
    z = Zone.objects.all().count()
    print(z,'--')
    a = Alert.objects.filter(status='ACTIVE').count()
    n = Notification.objects.all().count()
    return JsonResponse({"status":"ok","z":z,"a":a,"n":n})

from django.http import JsonResponse
from geopy.distance import geodesic
#
# def banzonealert_(request):
#     lid =request.POST['lid']
#     lat = float(request.POST['lat'])
#     lng = float(request.POST['lng'])
#
#     notifications = []
#
#     data = Banschedule.objects.all()
#
#     for i in data:
#         zone_lat = i.ZONE.latitude
#         zone_lng = i.ZONE.longitude
#
#         user_loc = (lat, lng)
#         zone_loc = (zone_lat, zone_lng)
#         print(user_loc)
#
#         dist_km = geodesic(user_loc, zone_loc).km
#
#         print(dist_km)
#
#         if dist_km <= 2 and i.status == 'Banned' :
#             notifications.append({
#                 "message": f"You are entering a banned zone ({dist_km:.2f} km)"
#             })
#
#     data=Fine()
#     data.date=datetime.datetime.now().date()
#     data.amount=1000
#     data.USERS=Users.objects.get(AUTHUSER=lid)
#     data.save()
#
#     if notifications:
#         return JsonResponse({
#             "status": "ok",
#             "notifications": notifications
#         })
#
#     return JsonResponse({"status": "no"})

#
# def banzonealert_(request):
#     lid = request.POST['lid']
#     lat = float(request.POST['lat'])
#     lng = float(request.POST['lng'])
#
#     notifications = []
#     user = Users.objects.get(AUTHUSER=lid)
#
#     data = Banschedule.objects.all()
#
#     for i in data:
#         zone_lat = i.ZONE.latitude
#         zone_lng = i.ZONE.longitude
#
#         user_loc = (lat, lng)
#         zone_loc = (zone_lat, zone_lng)
#
#         dist_km = geodesic(user_loc, zone_loc).km
#
#         if dist_km <= 2 and i.status == 'Banned':
#
#             # ✅ Create Fine
#             fine_amount = 1000
#             today = datetime.date.today()
#
#             Fine.objects.create(
#                 date=today,
#                 amount=fine_amount,
#                 USERS=user
#             )
#
#             # ✅ Send Email
#             subject = "⚠️ Banned Zone Alert & Fine Issued"
#             message = (
#                 f"Dear {user.name},\n\n"
#                 f"You have entered a banned fishing zone.\n\n"
#                 f"Distance from zone: {dist_km:.2f} km\n"
#                 f"Fine Amount: ₹{fine_amount}\n"
#                 f"Date: {today}\n\n"
#                 f"Please avoid restricted areas to prevent further penalties.\n\n"
#                 f"— Smart Fisheries Department"
#             )
#
#             send_mail(
#                 subject,
#                 message,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [user.email],
#                 fail_silently=False,
#             )
#
#             notifications.append({
#                 "message": f"You are entering a banned zone ({dist_km:.2f} km). Fine issued."
#             })
#
#             break  # 🚨 prevent multiple fines in same request
#
#     if notifications:
#         return JsonResponse({
#             "status": "ok",
#             "notifications": notifications
#         })
#
#     return JsonResponse({"status": "no"})


from django.http import JsonResponse
from geopy.distance import geodesic
import datetime
import smtplib

from .models import Users, Fine, Banschedule


def banzonealert_(request):
    try:
        lid = request.POST['lid']
        lat = float(request.POST['lat'])
        lng = float(request.POST['lng'])

        notifications = []

        user = Users.objects.select_related('BOATREGISTER').get(AUTHUSER=lid)

        bans = Banschedule.objects.filter(status='Banned')

        for ban in bans:
            zone_loc = (ban.ZONE.latitude, ban.ZONE.longitude)
            user_loc = (lat, lng)

            dist_km = geodesic(user_loc, zone_loc).km

            if dist_km <= 2:
                today = datetime.date.today()
                fine_amount = 1000

                already_fined = Fine.objects.filter(
                    USERS=user,
                    date=today
                ).exists()

                if not already_fined:
                    Fine.objects.create(
                        USERS=user,
                        date=today,
                        amount=fine_amount,
                        status='pending'
                    )

                    owneremail = user.BOATREGISTER.owneremail
                    print(owneremail,"ggggggggggggggg")
                    ownername = user.BOATREGISTER.ownername
                    print(ownername,"ttttttttttttttttt")

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("smartfisheries4@gmail.com", "tjtl lctl hhix ytki")

                    print("ttttttttttttttttt")

                    subject = "⚠️ Banned Zone Alert – Fine Issued"
                    message = (
                        f"Dear {ownername},\n\n"
                        f"Your boat has entered a restricted fishing zone.\n\n"
                        f"📍 Distance: {dist_km:.2f} km\n"
                        f"💰 Fine: ₹{fine_amount}\n"
                        f"📅 Date: {today}\n\n"
                        f"Please move away immediately.\n\n"
                        f"— Smart Fisheries Department"
                    )
                    print("uuuuuuuuuuuuuuuuuu")


                    msg = f"Subject: {subject}\n\n{message}"

                    server.sendmail("s@gmail.com", owneremail, msg)
                    print("ppppppppppppppppppppp")

                    server.quit()

                    print("eeeeeeeeeeeeeeeeeeeeee")


                notifications.append({
                    "message": f"You are going to enter a banned zone ({dist_km:.2f} km)."
                })
                break

        if notifications:
            return JsonResponse({"status": "ok", "notifications": notifications})

        return JsonResponse({"status": "no"})

    except Users.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Invalid user"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})



def boatowners(request):
    a=BoatRegister.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'boat_id':i.boatregistrationid,

                  })
    print(l)
    return JsonResponse({'status':'ok', 'data':l})



def view_fine(request):
    lid = request.POST['lid']
    a = Fine.objects.filter(USERS__AUTHUSER_id=lid)
    l = []
    for i in a:
        l.append({'id': i.id,
                  'date': i.date,
                  'amount':i.amount,
                  'status':i.status,

                  })
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def update_status(request):
    fid =request.POST['fid']
    Fine.objects.filter(id=fid).update(status='paid').order_by('-id')
    return JsonResponse({'status': 'ok'})




def forgot_password(request):
    return render(request,'forgot password.html')

def forgotpassword_post(request):


    email=request.POST['email']

    if User.objects.filter(username=email).exists():

        import random
        new_pass = random.randint(00000, 99999)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("smartfisheries4@gmail.com", "tjtl lctl hhix ytki")  # App Password
        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)  # Disconnect from the server
        server.quit()

        user = User.objects.get(username=email)
        user.set_password(str(new_pass))
        user.save()

        return redirect('/myapp/login_get/')
    else:
        messages.warning(request, 'email not  exists')
        return redirect('/myapp/forgot_password/')


def android_forget_password_post(request):
    email = request.POST.get('email')
    if not email:
        return JsonResponse({'status': 'error', 'message': 'Email is required'})

    try:
        user = User.objects.get(username=email)
        print(email,"fffffffffffffff")

        # Generate new password
        import random
        new_pass = str(random.randint(10000000, 99999999))
        user.password = make_password(str(new_pass))
        user.save()

        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "smartfisheries4@gmail.com"
        app_password = "tjtl lctl hhix ytki"

        subject = "Your New Password"
        body = f"Your new password is: {new_pass}"
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)
        server.quit()

        return JsonResponse({'status': 'ok', 'message': 'Password sent to your email'})

    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Email not found'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Email send error: {str(e)}'})



def help_update_status(request):
    req_id = request.POST['id']
    if not req_id:
        return JsonResponse({'status': 'error', 'message': 'Request ID missing'})
    f=Help.objects.get(id=req_id)
    f.status = 'Action taken'
    f.save()
    return JsonResponse({'status': 'ok', 'message': 'Status updated successfully'})



def user_sendcomplaint(request):
    complaint=request.POST['complaint']
    lid=request.POST['lid']


    obj=Complaint()
    obj.date=datetime.datetime.now().date()
    obj.status='pending'
    obj.reply="pending"
    obj.complaint=complaint
    obj.USERS=Users.objects.get(AUTHUSER_id=lid)
    obj.save()
    return JsonResponse({"status":"ok"})


def view_reply(request):
    lid = request.POST['lid']
    a = Complaint.objects.filter(USERS__AUTHUSER_id=lid).order_by('-id')
    l = []
    for i in a:
        l.append({
            'id': i.id,
                  'date': i.date,
                  'complaint':i.complaint,
                  'reply':i.reply,
                  'status':i.status,

                  })
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})