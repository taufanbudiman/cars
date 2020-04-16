from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

def index(request):
    return render(request, 'vehicle/index.html')


def frontlogin(request):
    msg = ""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('vehicle:index'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if username or password:
            if user.exists():
                user = user.last()
                if user.is_active == True:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse('login'))
                    else:
                        info = messages.ERROR
                        msg = "Pengguana / Kata sandi salah. silahkan coba kembali."
                else:
                    info = messages.INFO
                    msg = "User belum aktif, silahkan periksa email (Inbox/Spam) untuk mengaktifkan akun Anda."
            else:
                info = messages.INFO
                msg = "User tidak ditemukan"
        else:
            info = messages.WARNING
            msg = "Cek kembali pengguna/password Anda."
        messages.add_message(request, info, msg)

    return render(request, 'login.html')

def frontlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
