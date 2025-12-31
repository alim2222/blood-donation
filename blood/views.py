from django.shortcuts import render, redirect
from .models import Donor, BloodRequest
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

def home(request):
    donors = Donor.objects.all()
    requests = BloodRequest.objects.all()
    return render(request, 'home.html', {'donors': donors, 'requests': requests})
from django.shortcuts import render, redirect
from .models import Donor

def add_donor(request):
    if request.method == 'POST':
        donor = Donor.objects.create(
            name=request.POST['name'],
            blood_group=request.POST['blood_group'],
            phone=request.POST['phone'],
            location=request.POST['location'],
            last_donation_date=request.POST.get('last_donation_date') or None,
        )
        # donor add হওয়ার পর home page এ গিয়ে ঐ donor এ scroll করবে
        return redirect(f"/#donor-{donor.id}")

    # 👇 GET request হলে এইটা চলবে
    return render(request, 'add_donor.html')


def request_blood(request):
    if request.method == 'POST':
        BloodRequest.objects.create(
            patient_name=request.POST['patient_name'],
            blood_group=request.POST['blood_group'],
            hospital=request.POST['hospital'],
            phone=request.POST['phone'],
            needed_date=request.POST.get('needed_date')
        )
        return redirect('home')
    return render(request, 'request_blood.html')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign Up Successful!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required

# @login_required
# def home(request):
#     # your home view
#     return render(request, 'home.html')
# def donor_detail(request, id):
#     donor=Donor.objects.get(id=id)
#     return render(request, 'donor_detail.html',{'donor':donor})
# +  return render(request, 'home.html', {'donors': donors})
# def home(request):
#     donors = Donor.objects.all()
#     return render(request, 'home.html', {'donors': donors})
def home(request):
    donors = Donor.objects.all()
    requests = BloodRequest.objects.all().order_by('-id')
    return render(request, 'home.html', {
        'donors': donors,
        'requests': requests
    })