import re
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserInfoForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username",'first_name', 'last_name',"email", "password1", "password2")

class ResumeForm(forms.Form):
    user=forms.CharField(label='Username')
    name=forms.CharField(label='Name')
    image=forms.FileField(required=False)
    title=forms.CharField(label='Title')
    email=forms.EmailField(label='Email')
    mobile=forms.CharField(label='Mobile')
    linkedIn=forms.CharField(label='Linked In',required=False)

    profile=forms.CharField(label='Profile Summary')

    #College 
    academics_1_institute=forms.CharField(label='College')
    academics_1_program=forms.CharField(label='Program')
    academics_1_startDate=forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))
    academics_1_endDate=forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))
    academics_1_mark=forms.CharField(label='CGPA')
    #HS
    academics_2_institute=forms.CharField(label='School 1')
    academics_2_program=forms.CharField(label='Class')
    academics_2_startDate=forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))
    academics_2_endDate=forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))
    academics_2_mark=forms.CharField(label='Percentage')
    #LS
    academics_3_institute=forms.CharField(label='School 2')
    academics_3_program=forms.CharField(label='Class')
    academics_3_startDate=forms.DateField(label='Start Date',widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))
    academics_3_endDate=forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type':'date', 'max':datetime.now().date()}))
    academics_3_mark=forms.CharField(label='Percentage')

    areasOfInterest1=forms.CharField(label='Area of Interest 1')
    areasOfInterest2=forms.CharField(label='Area of Interest 2')
    areasOfInterest3=forms.CharField(label='Area of Interest 3', required=False)
    areasOfInterest4=forms.CharField(label='Area of Interest 4', required=False)
    
    paper_1=forms.CharField(required=False)
    paper_2=forms.CharField(required=False)

    #skills
    programmingLanguages=forms.CharField(label='Programming Languages')
    tools=forms.CharField(label='Tools and IDE')
    os=forms.CharField(label='Operating Systems')

    #projects
    project1_title=forms.CharField(label='Project Title 1')
    project1_toolUsed=forms.CharField(label='Tools Used')
    project2_title=forms.CharField(label='Project Title 2', required=False)
    project2_toolUsed=forms.CharField(label='Tools Used', required=False)
    project3_title=forms.CharField(label='Project Title 3',required=False)
    project3_toolUsed=forms.CharField(label='Tools Used',required=False)
    project4_title=forms.CharField(label='Project Title 4',required=False)
    project4_toolUsed=forms.CharField(label='Tools Used', required=False)

    address=forms.CharField(label='Address')
    achievement1=forms.CharField()
    achievement2=forms.CharField(required=False)
    achievement3=forms.CharField(required=False)
    achievement4=forms.CharField(required=False)

    strength1=forms.CharField()
    strength2=forms.CharField()
    strength3=forms.CharField(required=False)
    strength4=forms.CharField(required=False)
    strength5=forms.CharField(required=False)
    strength6=forms.CharField(required=False)
    strength7=forms.CharField(required=False)
    strength8=forms.CharField(required=False)

    language1=forms.CharField()
    language2=forms.CharField()
    language3=forms.CharField(required=False)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.helper.form_class = ' container justify-content-center '
        self.helper.form_method="post"
        self.helper.layout=Layout(
            Row(
                Column('user', css_class='form-group col-md-6  mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('name', css_class='form-group col-md-4  mb-10'),
                Column('image', css_class='form-group col-md-4  mb-10'),
                Column('title', css_class='form-group col-md-4 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('address', css_class='form-group col-md-7  mb-10'),
                Column('mobile', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('email', css_class='form-group col-md-6  mb-10'),
                Column('linkedIn', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            'profile',
            'academics_1_institute',
            Row(
                Column('academics_1_program', css_class='form-group col-md-6 mb-10'),
                Column('academics_1_mark', css_class='form-group col-md-2 mb-10'),
                Column('academics_1_startDate', css_class='form-group col-md-2 mb-10'),
                Column('academics_1_endDate', css_class='form-group col-md-2 mb-10'),
                css_class='form-row  center'
            ),
			'academics_2_institute',
            Row(
                Column('academics_2_program', css_class='form-group col-md-6 mb-10'),
                Column('academics_2_mark', css_class='form-group col-md-2 mb-10'),
                Column('academics_2_startDate', css_class='form-group col-md-2 mb-10'),
                Column('academics_2_endDate', css_class='form-group col-md-2 mb-10'),
                css_class='form-row  center'
            ),
            'academics_3_institute',
            Row(
                Column('academics_3_program', css_class='form-group col-md-6 mb-10'),
                Column('academics_3_mark', css_class='form-group col-md-2 mb-10'),
                Column('academics_3_startDate', css_class='form-group col-md-2 mb-10'),
                Column('academics_3_endDate', css_class='form-group col-md-2 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('areasOfInterest1', css_class='form-group col-md-3  mb-10'),
                Column('areasOfInterest2', css_class='form-group col-md-3 mb-10'),
                Column('areasOfInterest3', css_class='form-group col-md-3 mb-10'),
                Column('areasOfInterest4', css_class='form-group col-md-3 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('paper_1', css_class='form-group col-md-6  mb-10'),
                Column('paper_2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('programmingLanguages', css_class='form-group col-md-4  mb-10'),
                Column('tools', css_class='form-group col-md-4 mb-10'),
                Column('os', css_class='form-group col-md-4 mb-10'),
                css_class='form-row  center'
            ),
			Row(
                Column('project1_title', css_class='form-group col-md-7  mb-10'),
                Column('project1_toolUsed', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('project2_title', css_class='form-group col-md-7  mb-10'),
                Column('project2_toolUsed', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('project3_title', css_class='form-group col-md-7  mb-10'),
                Column('project3_toolUsed', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('project4_title', css_class='form-group col-md-7  mb-10'),
                Column('project4_toolUsed', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
        
            Row(
                Column('achievement1', css_class='form-group col-md-6  mb-10'),
                Column('achievement2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
		
            Row(
                Column('achievement3', css_class='form-group col-md-6  mb-10'),
                Column('achievement4', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),

            Row(
                Column('strength1', css_class='form-group col-md-3  mb-10'),
                Column('strength2', css_class='form-group col-md-3 mb-10'),
                Column('strength3', css_class='form-group col-md-3  mb-10'),
                Column('strength4', css_class='form-group col-md-3 mb-10'),
                css_class='form-row  center'
            ),
            
            Row(
                Column('strength5', css_class='form-group col-md-3  mb-10'),
                Column('strength6', css_class='form-group col-md-3 mb-10'),
                Column('strength7', css_class='form-group col-md-3  mb-10'),
                Column('strength8', css_class='form-group col-md-3 mb-10'),
                css_class='form-row  center'
            ),

            Row(
                Column('language1', css_class='form-group col-md-4  mb-10'),
                Column('language2', css_class='form-group col-md-4 mb-10'),
                Column('language3', css_class='form-group col-md-4 mb-10'),
                css_class='form-row  center'
            ),
            
			Submit('submit','Submit',css_class="btn-success")
			)