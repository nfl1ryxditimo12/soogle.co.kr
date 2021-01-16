from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            user = authenticate(username=username, nickname=nickname, password=password, email = email)

            login(request, user)

            return redirect('index')
        else:
            form = RegisterForm()

        return render(request, 'account/register.html', {'form': form})