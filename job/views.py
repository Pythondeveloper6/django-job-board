from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()


    paginator = Paginator(job_list, 25) # Show 25 contacts per page.

    context = {'jobs' :job_list } # template name
    return render(request,'job/job_list.html',context)



def job_detail(request , id):
    job_detail = Job.objects.get(id=id)
    context = {'job' : job_detail}
    return render(request,'job/job_detail.html',context)