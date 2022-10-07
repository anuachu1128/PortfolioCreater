from django.db import models

# Create your models here.
class Information(models.Model):
    user=models.CharField(max_length=50, default='')
    name=models.CharField(max_length=50, default='')
    title=models.CharField(max_length=50, default='')
    email=models.EmailField()
    mobile=models.CharField(max_length=50, default='')
    linkedIn=models.CharField(max_length=50, default='')

    profile=models.CharField(max_length=50, default='')

    #College 
    academics_1_institute=models.CharField(max_length=50, default='')
    academics_1_program=models.CharField(max_length=50, default='')
    academics_1_startDate=models.DateField()
    academics_1_endDate=models.DateField()
    academics_1_mark=models.CharField(max_length=50, default='')
    #HS
    academics_2_institute=models.CharField(max_length=50, default='')
    academics_2_program=models.CharField(max_length=50, default='')
    academics_2_startDate=models.DateField()
    academics_2_endDate=models.DateField()
    academics_2_mark=models.CharField(max_length=50, default='')
    #LS
    academics_3_institute=models.CharField(max_length=50, default='')
    academics_3_program=models.CharField(max_length=50, default='')
    academics_3_startDate=models.DateField()
    academics_3_endDate=models.DateField()
    academics_3_mark=models.CharField(max_length=50, default='')

    areasOfInterest1=models.CharField(max_length=50, default='')
    areasOfInterest2=models.CharField(max_length=50, default='')
    areasOfInterest3=models.CharField(max_length=50, default='')
    areasOfInterest4=models.CharField(max_length=50, default='')
    
    paper_1=models.CharField(max_length=50, default='')
    paper_2=models.CharField(max_length=50, default='')

    #skills
    programmingLanguages=models.CharField(max_length=50, default='')
    tools=models.CharField(max_length=50, default='')
    os=models.CharField(max_length=50, default='')

    #projects
    project1_title=models.CharField(max_length=50, default='')
    project1_toolUsed=models.CharField(max_length=50, default='')
    project2_title=models.CharField(max_length=50, default='')
    project2_toolUsed=models.CharField(max_length=50, default='')
    project3_title=models.CharField(max_length=50, default='')
    project3_toolUsed=models.CharField(max_length=50, default='')
    project4_title=models.CharField(max_length=50, default='')
    project4_toolUsed=models.CharField(max_length=50, default='')

    address=models.CharField(max_length=50, default='')
    achievement1=models.CharField(max_length=50, default='')
    achievement2=models.CharField(max_length=50, default='')
    achievement3=models.CharField(max_length=50, default='')
    achievement4=models.CharField(max_length=50, default='')

    strength1=models.CharField(max_length=50, default='')
    strength2=models.CharField(max_length=50, default='')
    strength3=models.CharField(max_length=50, default='')
    strength4=models.CharField(max_length=50, default='')
    strength5=models.CharField(max_length=50, default='')
    strength6=models.CharField(max_length=50, default='')
    strength7=models.CharField(max_length=50, default='')
    strength8=models.CharField(max_length=50, default='')

    language1=models.CharField(max_length=50, default='')
    language2=models.CharField(max_length=50, default='')
    language3=models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user + self.name