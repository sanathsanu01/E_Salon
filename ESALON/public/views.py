from django.shortcuts import render


# Create your views here.
def index(request):
    print("hiiiii")
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def saloonreg(request):
    return render(request,'saloonreg.html')

def about(request):
    return render(request,'about.html') 
               