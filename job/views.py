from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Job
from .form import ApplyForm,JobForm
from django.urls import reverse
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    paginator=Paginator(job_list,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    # context={"jobs":job_list}

    context={"jobs":page_obj,'job':job_list}#(job) use only for count
    return render(request,'job/job_list.html',context)


def job_details(request,slug):
    job_detail=Job.objects.get(slug=slug)

    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid:
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()

    else:
        form=ApplyForm

    context={"job":job_detail,'form':form}
    return render(request, 'job/job_detail.html',context)

def like_unlike(request,slug):
    job_detail=Job.objects.get(slug=slug)
    
    if request.user in job_detail.like.all():
        job_detail.like.remove(request.user)
        print("IN")
    else:
        job_detail.like.add(request.user)
        print("Not in")
    return redirect(reverse('jobs:job_details',kwargs={"slug":job_detail.slug}))


def add_job(request):

    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            # return redirect('/jobs/')
            return redirect(reverse('jobs:job_list'))

    else:
        form=JobForm
    context={'form':form}
    return render(request,'job/add_job.html',context)