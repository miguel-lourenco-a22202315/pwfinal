from django.shortcuts import render
from django.contrib.auth import models
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('https://a22202315.pythonanywhere.com/Login/login/')

    return render(request, 'login/registo.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'portfolio/index.html')
        else:
            render(request, 'login/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('https://a22202315.pythonanywhere.com/')