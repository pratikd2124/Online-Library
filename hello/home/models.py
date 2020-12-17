from django.db import models

# Create your models here.
class category(models.Model):
    
    category = models.CharField(max_length=25)
    def  __str__(self):
        return self.category
class Contact(models.Model):
    name = models.CharField(max_length=20)

    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=12)
    date = models.DateField()

    def __str__(self) :
        return self.name

class Library(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True)
    link = models.FileField( upload_to="pdf", max_length=100)
    
    def __str__(self):
        return self.name

class signup(models.Model):
    name = models.CharField(max_length=20)

    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

