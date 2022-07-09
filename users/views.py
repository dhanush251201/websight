from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from users.forms import UserForm , UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        messages.error(request,str(form.errors))
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account is created! You can now log in')
            return redirect('login')
    else:
        form = UserForm()
    return render(request,'users/signup.html', {'form':form})

def logout(request):
    auth_logout(request)
    return render(request,'users/logout.html')

def userSettings(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,f'Your Profile has been updated!')
            return redirect('settings')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request,'users/userSettings.html',context)

def profile(request):
    return render(request,'users/profile.html')

def deleteAccount(request):
    if request.method =='POST':
        user=User.objects.get(username=request.user.username)
        print(user)
        user.delete()
        return redirect('login')
    return render(request,'users/deleteAccount.html')


