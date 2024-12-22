from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form_action = reverse('contact:register')
    context = {
        'form': RegisterForm(),
        'form_action': form_action
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado')
            return redirect('contact:index')

        return render(
            request,
            'contact/register.html',
            context,
        )

    return render(
        request,
        'contact/register.html',
        context,
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )


@login_required(login_url='contact:index')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('contact:user_update')
