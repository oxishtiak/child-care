from django.contrib.auth import authenticate, login as signIn, logout as signOut
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
        return render(request, "accounts/register.html", {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                signIn(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {'form': form})

def logout(request):
    signOut(request)
    return redirect('home')