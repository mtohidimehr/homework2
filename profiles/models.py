from django.db import models

 
class Person(models.Model):
    firstName = models.CharField(max_length=20 )
    lastName = models.CharField(max_length=30)
    birthDay = models.DateField()
    mobileNamber = models.CharField(max_length=11)
    address =  models.CharField(max_length=100 )
    gender = models.CharField(max_length = 10)
   
       
    def __str__(self):
        return f"{self.lastName}, {self.firstName}"  
    
    class Meta:
       ordering = ("lastName", "firstName")
 
    
# Create your models here.
