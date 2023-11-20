
from schoolapp.models import Department,Course
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login

# Create your views here./
def index(request):
    return render(request,'home.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/new')
#         else:
#             messages.info(request,'invalid credential')
#             return redirect('/')
#     return render(request,'login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.check_password(password):
                auth_login(request, user)
                return redirect('/new')
            else:
                messages.error(request, 'Incorrect password')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmation_password = request.POST['confirmation_password']
        if not username or not password or not confirmation_password:
            messages.info(request, 'Please fill in all the required fields')
            return redirect('/register')
        if password == confirmation_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('/register')
            else:
                 user = User.objects.create_user(username=username,password=password)
                 user.save();
                 return redirect('/login')
        else:
            messages.info(request,'password not matched')
            return redirect('/register')
        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def allCourceDep(request):
    return render(request,'home.html')

def student_form(request):
    departments = Department.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html', {'message': 'Order Confirmed'})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form,'departments':departments, 'courses': courses})

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def new(request):
    return render(request,'new.html')
