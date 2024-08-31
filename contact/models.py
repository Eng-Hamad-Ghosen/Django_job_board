from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.email