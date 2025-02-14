from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')
        for error in list(form.errors.values()):
            print(request, error)
    else:
        form = UserRegistrationForm()
    return render(
        request,
        'register.html',
        {'form': form}
    )