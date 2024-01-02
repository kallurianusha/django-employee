from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Employee

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            try:
                employee = Employee.objects.get(username=username)
                messages.error(request, 'Username already exists.')
            except Employee.DoesNotExist:
                employee = Employee.objects.create(username=username, password=password)
                employee.save()
                messages.success(request, 'Account created successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            employee = Employee.objects.get(username=username, password=password)
            if employee:
                return redirect('dashboard')
        except Employee.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

    