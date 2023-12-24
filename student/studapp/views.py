from django.shortcuts import render,HttpResponse,redirect
from studapp.models import stud

# Create your views here.


def base (request):
    return render(request,'base.html')

def create(request):
    if request.method=="GET":
        return render(request,'create.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        age = request.POST['age']
        
        M = stud.objects.create(name=name, email=email, mobile=mobile, age=age)

        M.save()
       
        m = stud.objects.all()
        context ={}
        context['data'] = m
        return render(request,'dashboard.html',context)
    
def dashboard(request):
    m = stud.objects.all()
    context ={}
    context['data'] = m
    return render(request,'dashboard.html',context)

def delete(request,id):
    m = stud.objects.get(id=id)
    m.delete()
    return redirect('/dashboard')

def update(request,id):
    
    m = stud.objects.get(id=id)
    

    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        age = request.POST['age']
        
        m.name=name
        m.email=email
        m.mobile=mobile 
        m.age=age

        m.save()
        
        
        return redirect('/dashboard')
    
    context = {'students': m }
    return render(request,'update.html',context)
    
    