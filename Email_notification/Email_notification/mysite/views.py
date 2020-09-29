from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Application
from django.contrib.auth.decorators import login_required

# registration things


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('mysite:admin')
            else:
                return redirect('mysite:home')
        else:
            messages.info(request, '  Username OR password is incorrect. Try again')

    context = {}
    return render(request, 'registration/login.html', context)


def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mysite:login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('mysite:login')


@login_required(login_url='mysite:login')
def admin(request):
    return render(request, 'mysite/admin.html')


@login_required(login_url='mysite:login')
def home(request):
    return render(request, 'mysite/home.html')


@login_required(login_url='mysite:login')
def forms(request):
    return render(request, 'mysite/Forms.html')


@login_required(login_url='mysite:login')
def add_application_form_submission(request):

    first_name = request.POST["inputFirstname"]
    second_name = request.POST["inputSecondname"]
    email = request.POST["inputEmail4"]
    phone_no = request.POST["inputPhoneno"]
    address = request.POST["inputAddress"]
    city = request.POST["inputCity"]
    job_type = request.POST["inputType"]
    job_experience = request.POST["inputexperience"]

    # adding application to database
    application = Application(first_name=first_name, second_name=second_name, email=email, phone_no=phone_no,
                              address=address, city=city, job_type=job_type, job_experience=job_experience)
    application.save()

    return render(request, 'mysite/Forms.html', {'first_name': first_name, 'second_name': second_name})
