from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def receipes(requets):


    if requets.method=="POST":
        data=requets.POST
        receipe_name=data.get('receipe_name')
        receipe_dis=data.get('receipe_dis')
        receipe_img=requets.FILES.get('receipe_img')
        Vege.objects.create(
            receipe_name=receipe_name,
            receipe_dis=receipe_dis,
            receipe_img=receipe_img


        )
        return redirect('/receipes')
    queryset=Vege.objects.all()
    if requets.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=requets.GET.get('search'))
        


    context={'receipes':queryset}





    return render(requets,'reciepes.html',context)

@login_required(login_url="/login/")
def update(requets,id):
    queryset=Vege.objects.get(id=id)
    if requets.method=="POST":
        data=requets.POST

        receipe_name=data.get('receipe_name')
        receipe_dis=data.get('receipe_dis')
        receipe_img=requets.FILES.get('receipe_img')
        
        queryset.receipe_name=receipe_name
        queryset.receipe_dis=receipe_dis

        if receipe_img:
            queryset.receipe_img=receipe_img

        queryset.save()    
        return redirect('/receipes/')
    context={'receipe':queryset}
    return render(requets,'update.html',context)


# def delete_receipe(requets,id):
#     queryset=Vege.objects.get(id=id)
#     queryset.delete()
#     return redirect('/receipes/') 

@login_required(login_url="/login/")
def delete_receipe(request, id):
    recipe = Vege.objects.get(id=id)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('/receipes/')
    
    return render(request, 'reciepes.html', {'recipe': recipe})


def login_page(requests):
    if requests.method=="POST":
        username=requests.POST.get('username')
        password=requests.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(requests,'Invalid Username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(requests,'Invalid username')
            return redirect('/login/')
        else:
            login(requests,user)
            return redirect('/receipes/')

    return render(requests,'login.html')

def logout_page(requests):
    logout(requests)
    return redirect('/login/')

def register_page(requests):
    if requests.method=="POST":
        first_name=requests.POST.get('first_name')
        last_name=requests.POST.get('last_name')
        username=requests.POST.get('username')
        password=requests.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(requests, "User Exist")
            return redirect('/register/')


        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.error(requests, "Account Created Succesfully")
        return redirect('/register/')

    return render(requests,'register.html')