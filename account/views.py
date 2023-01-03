from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from account.forms import *
from jobapp.permission import employee


def get_success_url(request):
    """
    Handle Success Url After LogIN

    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('jobapp:home')


def employee_registration(request):
    """
    Handle Employee Registration

    """
    form = EmployeeRegistrationForm(
        request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context = {

        'form': form
    }

    return render(request, 'account/employee-registration.html', context)


def employer_registration(request):
    """
    Handle Employee Registration 

    """

    form = EmployerRegistrationForm(
        request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context = { 
        'form': form
    }

    return render(request, 'account/employer-registration.html', context)


def employer_edit_profile(request, id=id):
    """
    Handle Employer Profile Update Functionality

    """

    user = get_object_or_404(User, id=id)
    form = EmployerProfileEditForm(
        request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:employer-profile", kwargs={
            'id': form.id
        }))
    context = {
        'user': user,
        'form': form
    }

    return render(request, 'account/employer-edit-profile.html', context)


@login_required(login_url=reverse_lazy('accounts:login'))
# @employee
def employee_edit_profile(request, id=id):
    """
    Handle Employee Profile Update Functionality

    """

    user = get_object_or_404(User, id=id)
    form = EmployeeProfileEditForm(
        request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:edit-profile", kwargs={
            'id': form.id
        }))
    context = {
        'user': user,
        'form': form
    }

    return render(request, 'account/employee-edit-profile.html', context)

@login_required(login_url=reverse_lazy('accounts:login'))
# @employee
def employee_edit_password(request, id=id):

    instance_user = get_object_or_404(User, id=int(id))
    form_edit_password = EmployeeChangePassword(instance_user, data=request.POST or None)


    if form_edit_password.is_valid():
       form_edit_password.save()
       messages.success(request, 'Your Password Was Successfully Updated!')

    context={'form_edit_password': form_edit_password}

    return render(request, 'account/change-password.html', context)



def user_logIn(request):
    """
    Provides users to logIn

    """

    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request, 'account/login.html', context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')
