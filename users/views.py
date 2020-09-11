from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView

from .forms import UserRegForm


class Registration(CreateView):

    def post(self, request):
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Пользователь {username} был успешно создан")
            return redirect("log")
        data = {'form': form, 'title': 'Регистрация пользователя'}
        return render(request, 'users/registration.html', data)

    def get(self,  request):
        form = UserRegForm()
        view = {"form": form, "title": "Регистрация пользователя"}
        return render(request, "users/registration.html", view)



