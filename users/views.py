from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile


def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    """Custom login view."""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


@login_required
def profile(request):
    """User profile view."""
    # Profile should be created automatically via signal, but use get_or_create as fallback
    profile_obj, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_obj)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileUpdateForm(instance=profile_obj)
    
    return render(request, 'users/profile.html', {'form': form, 'profile': profile_obj})


class CustomPasswordChangeView(PasswordChangeView):
    """Custom password change view."""
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:profile')

