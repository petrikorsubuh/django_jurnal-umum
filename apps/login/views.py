from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from apps.login.forms import LoginForm
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

class LoginView(View):
    template_name = 'auth/login.html'
    
    def get(self, request):
        return render(request, self.template_name,)

class LoginProccessView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            if user:
                login(request,user)
                return redirect('/jurnal')
            messages.error(request,'username dan password tidak di temukan')
            return redirect('/login')
        messages.error(request,'form login harus di isi')
        return redirect('/login')


class LogOutView(View):
    def get(self, reques):
        logout(reques)

        return redirect('/login')
