from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from hello.models import Shop
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# from django.views.generic import 



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        return render(request, "signin.html", {'form': form})

@login_required()
def profile(request):
    if request.method == 'POST':
        pass
    else:
        context = {
            'shops': Shop.objects.filter(ownerProfile = request.user.id)
        }
        return render(request, "profile.html", context)


# class profileDetailList(DetailView):


@login_required()
def update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, "update.html", context={'u_form': user_form, 'p_form': profile_form})