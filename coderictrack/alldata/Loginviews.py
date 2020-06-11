from django.shortcuts import render,HttpResponse, redirect
from .storemodels import Employee
from .storework import Worksubmit
# Create your views here.
def login(request):
    if request.method == 'POST' and 'submit1' in request.POST:
        U_ID=request.POST.get('U')
        passwords=request.POST.get('Passw')
        print('Logined')
        try:
            password=Employee.objects.get(Unique_ID=U_ID)
            global id
            id=password.Unique_ID
            pswd=password.Password
            global username
            username=password.Employee_Name
            print('Try in button 1')
            if id == U_ID and pswd == passwords:
                print('Match')
                print(username)
                context={
                    'data': id,
                    'displayname': username,
                    }
                return render(request,'Work.html',context)
                #return redirect('work/',id=U_ID)
            else:
                return render(request,'erroruser.html')
                print('else')
        except:
            print('None')
            return render(request,'erroruser.html')
            #return render(request,'Login.html')
    if request.method == 'POST' and 'submit2' in request.POST:
        try:
            print('Try in button 2')
            dates=request.POST.get('dates')
            id=request.POST.get('unique')
            fromhour=request.POST.get('from')
            leader=request.POST.get('leader')
            mentor=request.POST.get('mentor')
            member=request.POST.get('member')
            description=request.POST.get('description')
            tohour=request.POST.get('to')
            print('html date: ',dates)
            print('html work id:',id)
            print('html from hour:' ,fromhour)
            print('html leader:' ,leader)
            print('html mentor:' ,mentor)
            print('html member:' ,member)
            print('html dscription:' ,description)
            print('html tohour:' ,tohour)
            print('submitted')
            if id != "":
                user=Worksubmit()
                user.work_date=dates
                user.uniqueID=id
                user.work_from=fromhour
                user.Team_Leader=leader
                user.Mentor=mentor
                user.Member_Name=member
                user.Work_Description=description
                user.work_to=tohour
                user.save()
                context={
                    'displayname' : username,
                    'data': id,
                }
                return render(request,'Work.html',context)
            else:
                print('Field is null')
        except:
            print('Button 2 Error')
    # Logout Button
    if request.method == 'POST' and 'logout' in request.POST:
        try:
            print('Try in logout')
            return redirect('/')
        except:
            print('except in logout')
    # Submission Button
    if request.method == 'POST' and 'submission' in request.POST:
        context={
            'displayname' : username,
            'data': id,
        }
        print(context)
        return render(request,'Work.html',context)
    # History Button
    if request.method == 'POST' and 'history' in request.POST:
        workers_datas=Worksubmit.objects.all().filter(uniqueID=id)
        print(workers_datas)

        context={
            'displayname' : username,
            'whole_data':workers_datas,
        }
        return render(request,'History.html',context)
    return render(request,'Login.html')
