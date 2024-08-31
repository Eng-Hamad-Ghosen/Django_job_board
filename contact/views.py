from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_message(request):
    myContact=Info.objects.first()
    if request.method=='POST':
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        print(subject)
        print(email)
        print(message)
        # subject = 'Thank you for registering to our site'
        # message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]   
        
        send_mail( subject,
                  message,
                  email_from,
                  recipient_list )  
        

    return render(request,'contact/contact.html',{'myContact':myContact})