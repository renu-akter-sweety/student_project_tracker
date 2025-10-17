from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    student_name=models.CharField(max_length=100,null=True)
    student_id=models.IntegerField(null=True)
    def __str__(self):
        return self.username
class ProjectModel(models.Model):
      PROJECT_STATUS=[
           ('NotStarted','NotStarted'),
           ('InProgress','InProgress'),
           ('Completed','Completed'),
      ]
    
      project_name=models.CharField(max_length=100,null=True) 
      project_description =models.TextField(null=True)
      project_status=models.CharField(null=True,max_length=100,choices=PROJECT_STATUS)
      deadline=models.DateField(null=True)
      thumbnail=models.ImageField(upload_to='media/project_image',null=True)
      created_by=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='created_by')
      def __str__(self):
        return self.project_name

