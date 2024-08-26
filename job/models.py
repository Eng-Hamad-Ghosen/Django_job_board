from django.db import models
from  django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Port Time','Port Time'),
)

def image_upload(instance,filename):
    imagename , extention=filename.split(".")#picture.png
    # return "jobs/%s/%s.%s"%(instance.id,instance.id,extention)
    # return "jobs/%s.%s"%(instance.salary,extention)
    return "jobs/%s.%s"%(instance.id,extention)

class Job(models.Model):
    like=models.ManyToManyField(User,blank=True)
    
    owner=models.ForeignKey(User, related_name=("Job_Owner"), on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    # location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now_add=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    # image = models.ImageField(upload_to='jobs/')
    image = models.ImageField(upload_to=image_upload)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    slug= models.SlugField(blank=True,null=True)\

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job =  models.ForeignKey('Job', on_delete=models.CASCADE,related_name='Apply_Job')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='applay/')
    cover_letter = models.TextField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
