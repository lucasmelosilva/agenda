from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm


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


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
