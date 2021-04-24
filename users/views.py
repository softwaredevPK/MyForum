from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def profile(request):
    return render(request, 'users/profile.html')
