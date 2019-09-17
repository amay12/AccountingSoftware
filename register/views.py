from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def logout_view(request):
    logout(request)
    return redirect('register:register')


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'Contacts/userlogin.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # cleaned/normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # returns user objects if credentials are correct
            user = authenticate(username= username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    # username = request.session['username']
                    return redirect('Dashboard:dashboard-index')

        return render(request, self.template_name, {'form': form})


def login_view(request):
    template_name= 'Contacts/login_view.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'Contacts/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned/normalized data
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username= username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    # username = request.session['username']
                    return redirect('Dashboard:dashboard-index')

        return render(request, self.template_name, {'form': form})






