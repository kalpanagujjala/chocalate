from django.shortcuts import render
from coco.models import Menu
from django.contrib.auth.models import User

# Create your views here.
def fun(request,no,cost,):
    obj=Menu.objects.get(id=no)
    return render(request,"index.html",{'res':cost})

def userViews(request):
    result=User.objects.all()
    return render(request,'home.html',{'res':result})
def callviews(request):
    if request.method=='POST':
        usern=request.POST.get('user')
        check=User.objects.filter(username=usern).exists()
        print(check)
    return render(request,'call.html')