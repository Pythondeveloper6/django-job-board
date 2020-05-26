from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    print(job_list)
    context = {'jobs' :job_list }
    return render(request,'job/job_list.html',context)



def job_detail(request , id):
    pass