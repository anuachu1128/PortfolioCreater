from django.shortcuts import render,redirect
from .forms import ResumeForm,UserInfoForm
from django.http import HttpResponse
import os
from ResumeApp.models import Information
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django import forms


# Create your views here.
def home(request):
    my_dict={'var1': 'Login/Register',
                'var2': 'Create Your Perfect Porfolio',
                'var3': '',
                'var4':'',
                'var5':'Register',
                'var6':'Login',
                'var7':'Get Started',
                'var8': 'register',
                'var9': ''}
    return render(request,'home.html', context=my_dict)

def homePage(request):
    my_dict={'var1': 'Welcome '+request.user.username,
            'var2': 'Start Creating Your Own Porfolio',
            'var3': 'Add/Edit Resume',
            'var4':  'View Resume',
            'var5':'Logout',
            'var6':' ',
            'var7':'Create Portfolio',
            'var8': ' ',
            'var9': 'Home'}
    return render(request,'home.html', context=my_dict)


def registerPage(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            my_dict={'var1': 'Welcome '+form.cleaned_data.get('username'),
            'var2': 'Start Creating Your Own Porfolio',
            'var3': 'Add/Edit Resume',
            'var4':  'View Resume',
            'var5':'Logout',
            'var6':' ',
            'var7':'Create Portfolio',
            'var8': ' '}
            return render(request, 'home.html', context=my_dict)
    else:
        form = UserInfoForm()
    return render (request=request, template_name="register.html", context={"registerForm":form})

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                my_dict={'var1': 'Welcome '+form.cleaned_data.get('username'),
                'var2': 'Start Creating your Porfolio',
                'var3': 'Add/Edit Resume',
                'var4':  'View Resume',
                'var5':'Logout',
                'var6':' ',
                'var7':'Create Portfolio',
                'var8': ' '}
                return render(request, 'home.html', context=my_dict)
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"loginForm":form})

def logoutPage(request):
    logout(request)
    return redirect("/login/")

def fileUpload(f):  
    filePath=os.path.join(os.getcwd(),'static',f.name)
    with open(filePath, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  

def fill(request):
    if request.method == 'POST':
        form=ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            fileUpload(request.FILES["image"])
            title=form.cleaned_data['title']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            linkedIn=form.cleaned_data['linkedIn']

            profile=form.cleaned_data['profile']

            academics_1_institute=form.cleaned_data['academics_1_institute']
            academics_1_program=form.cleaned_data['academics_1_program']
            academics_1_startDate=form.cleaned_data['academics_1_startDate']
            academics_1_endDate=form.cleaned_data['academics_1_endDate']
            academics_1_mark=form.cleaned_data['academics_1_mark']

            academics_2_institute=form.cleaned_data['academics_2_institute']
            academics_2_program=form.cleaned_data['academics_2_program']
            academics_2_startDate=form.cleaned_data['academics_2_startDate']
            academics_2_endDate=form.cleaned_data['academics_2_endDate']
            academics_2_mark=form.cleaned_data['academics_2_mark']

            academics_3_institute=form.cleaned_data['academics_3_institute']
            academics_3_program=form.cleaned_data['academics_3_program']
            academics_3_startDate=form.cleaned_data['academics_3_startDate']
            academics_3_endDate=form.cleaned_data['academics_3_endDate']
            academics_3_mark=form.cleaned_data['academics_3_mark']

            areasOfInterest1=form.cleaned_data['areasOfInterest1']
            areasOfInterest2=form.cleaned_data['areasOfInterest2']
            areasOfInterest3=form.cleaned_data['areasOfInterest3']
            areasOfInterest4=form.cleaned_data['areasOfInterest4']

            paper_1=form.cleaned_data['paper_1']
            paper_2=form.cleaned_data['paper_2']

            programmingLanguages=form.cleaned_data['programmingLanguages']
            tools=form.cleaned_data['tools']
            os=form.cleaned_data['os']

            project1_title=form.cleaned_data['project1_title']
            project1_toolUsed=form.cleaned_data['project1_toolUsed']
            project2_title=form.cleaned_data['project2_title']
            project2_toolUsed=form.cleaned_data['project2_toolUsed']
            project3_title=form.cleaned_data['project3_title']
            project3_toolUsed=form.cleaned_data['project3_toolUsed']
            project4_title=form.cleaned_data['project4_title']
            project4_toolUsed=form.cleaned_data['project4_toolUsed']
           

            address=form.cleaned_data['address']
            achievement1=form.cleaned_data['achievement1']
            achievement2=form.cleaned_data['achievement2']
            achievement3=form.cleaned_data['achievement3']
            achievement4=form.cleaned_data['achievement4']

            strength1=form.cleaned_data['strength1']
            strength2=form.cleaned_data['strength2']
            strength3=form.cleaned_data['strength3']
            strength4=form.cleaned_data['strength4']
            strength5=form.cleaned_data['strength5']
            strength6=form.cleaned_data['strength6']
            strength7=form.cleaned_data['strength7']
            strength8=form.cleaned_data['strength8']

            language1=form.cleaned_data['language1']
            language2=form.cleaned_data['language2']
            language3=form.cleaned_data['language3']
            if Information.objects.filter(user=request.user.username).exists():
                for i in Information.objects.filter(user=request.user.username):
                    i.name=name
                    i.title=title
                    i.email=email
                    i.mobile=mobile
                    i.linkedIn=linkedIn
                    i.profile=profile
                    i.academics_1_institute=academics_1_institute
                    i.academics_1_program=academics_1_program
                    i.academics_1_startDate=academics_1_startDate
                    i.academics_1_endDate=academics_1_endDate
                    i.academics_1_mark=academics_1_mark
                    i.academics_2_institute=academics_2_institute
                    i.academics_2_program=academics_2_program
                    i.academics_2_startDate=academics_2_startDate
                    i.academics_2_endDate=academics_2_endDate
                    i.academics_2_mark=academics_2_mark
                    i.academics_3_institute=academics_3_institute
                    i.academics_3_program=academics_3_program
                    i.academics_3_startDate=academics_3_startDate
                    i.academics_3_endDate=academics_3_endDate
                    i.academics_3_mark=academics_3_mark
                    i.areasOfInterest1=areasOfInterest1
                    i.areasOfInterest2=areasOfInterest2
                    i.areasOfInterest3=areasOfInterest3
                    i.areasOfInterest4=areasOfInterest4
                    i.paper_1=paper_1
                    i.paper_2=paper_2
                    i.address=address
                    i.achievement1=achievement1
                    i.achievement2=achievement2
                    i.achievement3=achievement3
                    i.achievement4=achievement4
                    i.strength1=strength1
                    i.strength2=strength2
                    i.strength3=strength3
                    i.strength4=strength4
                    i.strength5=strength5
                    i.strength6=strength6
                    i.strength7=strength7
                    i.strength8=strength8
                    i.language1=language1
                    i.language2=language2
                    i.language3=language3
                    i.save()
                
            else:
                print(request.user.username)
                newInfo=Information(user=request.user.username, name=name, title=title, email= email, mobile=mobile, linkedIn= linkedIn, profile= profile,
                    academics_1_institute=academics_1_institute, academics_1_program=academics_1_program, academics_1_startDate=academics_1_startDate, academics_1_endDate=academics_1_endDate, academics_1_mark=academics_1_mark,
                    academics_2_institute=academics_2_institute, academics_2_program=academics_2_program, academics_2_startDate=academics_2_startDate,academics_2_endDate=academics_2_endDate,academics_2_mark=academics_2_mark,
                    academics_3_institute=academics_3_institute, academics_3_program=academics_3_program, academics_3_startDate=academics_3_startDate,academics_3_endDate=academics_3_endDate,academics_3_mark=academics_3_mark, 
                    areasOfInterest1=areasOfInterest1, areasOfInterest2=areasOfInterest2, areasOfInterest3=areasOfInterest3, areasOfInterest4=areasOfInterest4,
                    paper_1=paper_1, paper_2=paper_2,
                    programmingLanguages=programmingLanguages, tools=tools, os=os,
                    project1_title=project1_title, project1_toolUsed=project1_toolUsed,
                    project2_title=project2_title, project2_toolUsed=project2_toolUsed,
                    project3_title=project3_title, project3_toolUsed=project3_toolUsed,
                    project4_title=project4_title, project4_toolUsed=project4_toolUsed,
                    address=address,
                    achievement1=achievement1, achievement2=achievement2, achievement3=achievement3, achievement4=achievement4,
                    strength1=strength1, strength2=strength2, strength3=strength3, strength4=strength4,
                    strength5=strength5, strength6=strength6, strength7=strength7, strength8=strength8,
                    language1=language1, language2=language2, language3=language3)
                newInfo.save()


            details={'name':name, 'title':title, 'email': email, 
                    'mobile':mobile, 'linkedIn': linkedIn, 'profile': profile,
                    'academics_1_institute':academics_1_institute, 'academics_1_program':academics_1_program, 'academics_1_startDate':academics_1_startDate, 'academics_1_endDate':academics_1_endDate, 'academics_1_mark':academics_1_mark,
                    'academics_2_institute':academics_2_institute, 'academics_2_program':academics_2_program, 'academics_2_startDate':academics_2_startDate, 'academics_2_endDate':academics_2_endDate, 'academics_2_mark':academics_2_mark,
                    'academics_3_institute':academics_3_institute, 'academics_3_program':academics_3_program, 'academics_3_startDate':academics_3_startDate, 'academics_3_endDate':academics_3_endDate, 'academics_3_mark':academics_3_mark, 
                    'areasOfInterest1':areasOfInterest1, 'areasOfInterest2':areasOfInterest2, 'areasOfInterest3':areasOfInterest3, 'areasOfInterest4': areasOfInterest4,
                    'paper_1':paper_1, 'paper_2':paper_2,
                    'programmingLanguages':programmingLanguages, 'tools':tools, 'os':os,
                    'project1_title':project1_title, 'project1_toolUsed':project1_toolUsed,
                    'project2_title':project2_title, 'project2_toolUsed':project2_toolUsed,
                    'project3_title':project3_title, 'project3_toolUsed':project3_toolUsed,
                    'project4_title':project4_title, 'project4_toolUsed':project4_toolUsed,
                    'address': address,
                    'achievement1':achievement1, 'achievement2':achievement2, 'achievement3':achievement3, 'achievement4':achievement4,
                    'strength1':strength1, 'strength2':strength2, 'strength3':strength3, 'strength4':strength4,
                    'strength5':strength5, 'strength6':strength6, 'strength7':strength7, 'strength8':strength8,
                    'language1':language1, 'language2':language2, 'language3':language3}
            return render(request,'resume.html',details)
    else:
        form=ResumeForm()
    return render(request,'resumeDetails.html',{'form':form})

def resume(request):
    if request.user:
        my_dict={'var1': 'Welcome '+request.user.username,
            'var2': 'Start Creating Your Own Porfolio',
            'var3': 'Add/Edit Resume',
            'var4':  'View Resume',
            'var5':'Logout',
            'var6':' ',
            'var7':'Create Portfolio',
            'var8': ' '}
    else:
        my_dict={'var1': 'Login/Register',
                'var2': 'Create Your Perfect Porfolio',
                'var3': '',
                'var4':'',
                'var5':'Register',
                'var6':'Login',
                'var7':'Get Started',
                'var8': 'register'}
    if Information.objects.filter(user=request.user.username).exists():
        for i in Information.objects.filter(user=request.user.username):
            dictionary={"name":i.name, 'image':' ', 'title':i.title, 'email': i.email, 
                        'mobile':i.mobile, 'linkedIn': i.linkedIn, 'profile': i.profile,
                        'academics_1_institute':i.academics_1_institute, 'academics_1_program':i.academics_1_program, 'academics_1_startDate':i.academics_1_startDate, 'academics_1_endDate':i.academics_1_endDate, 'academics_1_mark':i.academics_1_mark,
                        'academics_2_institute':i.academics_2_institute, 'academics_2_program':i.academics_2_program, 'academics_2_startDate':i.academics_2_startDate, 'academics_2_endDate':i.academics_2_endDate, 'academics_2_mark':i.academics_2_mark,
                        'academics_3_institute':i.academics_3_institute, 'academics_3_program':i.academics_3_program, 'academics_3_startDate':i.academics_3_startDate, 'academics_3_endDate':i.academics_3_endDate, 'academics_3_mark':i.academics_3_mark, 
                        'areasOfInterest1':i.areasOfInterest1, 'areasOfInterest2':i.areasOfInterest2, 'areasOfInterest3':i.areasOfInterest3, 'areasOfInterest4': i.areasOfInterest4,
                        'paper_1':i.paper_1, 'paper_2':i.paper_2,
                        'programmingLanguages':i.programmingLanguages, 'tools':i.tools, 'os':i.os,
                        'project1_title':i.project1_title, 'project1_toolUsed':i.project1_toolUsed,
                        'project2_title':i.project2_title, 'project2_toolUsed':i.project2_toolUsed,
                        'project3_title':i.project3_title, 'project3_toolUsed':i.project3_toolUsed,
                        'project4_title':i.project4_title, 'project4_toolUsed':i.project4_toolUsed,
                        'address': i.address,
                        'achievement1':i.achievement1, 'achievement2':i.achievement2, 'achievement3':i.achievement3, 'achievement4':i.achievement4,
                        'strength1':i.strength1, 'strength2':i.strength2, 'strength3':i.strength3, 'strength4':i.strength4,
                        'strength5':i.strength5, 'strength6':i.strength6, 'strength7':i.strength7, 'strength8':i.strength8,
                        'language1':i.language1, 'language2':i.language2, 'language3':i.language3}
        return render(request, 'resume.html', dictionary)
    else:
        return render(request, 'noResume.html', my_dict)





        
