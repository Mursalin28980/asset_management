from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Asset

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('assigned_assets')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def assigned_assets(request):
    user = request.user
    assets = Asset.objects.filter(user=user)
    return render(request, 'assigned_assets.html', {'assets': assets})

def choose_page(request):
    return render(request, 'choose_page.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Handle form submission for updating user information
        # Retrieve the submitted data and update the user's information
        user = request.user
        user.name = request.POST['name']
        user.set_password(request.POST['password'])
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('edit_profile')
    else:
        return render(request, 'edit_profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        user = request.user
        if user.check_password(current_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been changed successfully.')
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Invalid current password.')

    return render(request, 'change_password.html')