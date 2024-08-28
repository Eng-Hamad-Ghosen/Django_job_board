from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile= models.CharField(max_length=15)
    image=models.ImageField(upload_to='profile/')
    city= models.ForeignKey('City', related_name='profile_city', on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.user.username
 
#مشان وقت المستخدم يعمل signup لازم ينعلمو profile 
#متل فكرة انشاء Token تلقائيا 
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def auto_create_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)
    
class City(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    