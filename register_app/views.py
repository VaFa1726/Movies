from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  # ایجاد پروفایل اختصاصی
            login(request, user)  # ورود خودکار
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
