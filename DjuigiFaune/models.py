from django.db import models

# Create your models here.
class Animaux(models.Model):
    file=models.FileField(upload_to="animaux/")
    description=models.TextField()
    prix=models.IntegerField()
    numero=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description[:20]
    


class Contact(models.Model):
    wathsApp=models.CharField(max_length=500,null=True,blank=True)
    facebook=models.CharField(max_length=500,null=True,blank=True)
    email=models.CharField(max_length=500,null=True,blank=True)
    telephone1=models.CharField(max_length=500,null=True,blank=True)
    telephone2=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return "Mes contacts"
    
