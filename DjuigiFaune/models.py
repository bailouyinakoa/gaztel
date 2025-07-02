import os
from django.db import models

# Create your models here.
class Animaux(models.Model):
    file=models.FileField(upload_to="animaux/")
    description=models.TextField()
    prix=models.IntegerField()
    numero=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def filename(self):
        if self.file:
            try:
                return os.path.basename(self.file.name)
            except:
                pass
        else:
            return None

    class Meta:
        pass
    @property
    def is_image(self):
        try:
            if self.filename.lower().endswith((".jpg",".jpeg",".png",".gif",".svg",".webp")):
                return True
            else:
                return False
        except:
            pass
    @property
    def is_video(self):
        try:
            if self.filename.lower().endswith((".mp4",".avi",".mov",".mkv")):
                return True
            else:
                return False
        except:
            pass


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
    
