from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class profession(models.Model):
    name = models.CharField(max_length=50)
    profession=models.CharField(max_length=50)
    

def __str__(self):
        return self.name

class contact(models.Model):
    
    Name=models.CharField('Name', max_length=200)
    E_mail=models.EmailField('E-Mail', blank=False)
    phone_number = PhoneNumberField('Phone-Number',null=True, blank=True)
    

    
    Description= models.TextField('Your message Request', max_length=200)


    def __str__(self):
        return self.Name
    

