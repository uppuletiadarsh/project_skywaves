from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request,'home.html')
def home_page(request):
    return render(request,'home_page.html')
def reg(request):
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
# registration/views.py



# Application1/views.py

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def save(request):
    if request.method == 'POST':
        # Retrieve form data from request.POST
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        mobile_number = request.POST['mobileNumber']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        # Perform basic validation (you may want to add more validation)
        if password != confirmPassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Create a new User object and save it
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            email=email,
            gender=gender,
            password=password  # Note: In production, use Django's password hashing mechanisms
        )
        new_user.save()

        # Redirect to a success page
        return redirect('success')  # You should define this URL in your urls.py
    else:
        return render(request, 'registration.html')


# Application1/views.py

from django.shortcuts import render, redirect
from django.contrib import messages

# Application1/views.py


def success(request):
    return render(request, 'success.html')
def dashboard(request):
    return render(request, 'dashboard.html')

# Application1/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import User

def logi(request):
    if request.method == 'POST':
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']

        try:
            user = User.objects.get(mobile_number=mobile_number)
        except User.DoesNotExist:
            messages.error(request, "Invalid mobile number or password.")
            return redirect('login')

        # Check if the password matches
        if not check_password(password, user.password):
            messages.error(request, "Invalid mobile number or password.")
            return redirect('login')

        # Log the user in (for demonstration purposes, you can implement session management as per Django's guidelines)
        request.session['user_id'] = user.id  # Store user ID in session

        # Redirect to a dashboard or profile page
        return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL

    # If it's a GET request or initial load, render the login form
    return render(request, 'login.html')

