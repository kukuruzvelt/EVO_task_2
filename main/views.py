from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Usernames
from .forms import UsernamesForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = UsernamesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get("name")
            request.session['_old_post'] = request.POST
            try:
                Usernames.objects.get(name=data)
                return HttpResponseRedirect('existing_user')
            except Usernames.DoesNotExist as e:
                form.save()
                return HttpResponseRedirect('new_user')
        else:
            error = 'Виникла помилка'
    form = UsernamesForm()
    return render(request, 'main/index.html', {"form": form, 'error': error})


def all_users(request):
    names = Usernames.objects.all()
    return render(request, 'main/all_users.html', {'title': 'Список користувачів', 'usernames': names})


def existing_user(request):
    old_post = request.session.get('_old_post')
    name = old_post['name']
    return render(request, 'main/user.html', {'title': 'Новий користувач', 'text': f'Вже бачилися, {name}'})


def new_user(request):
    old_post = request.session.get('_old_post')
    name = old_post['name']
    return render(request, 'main/user.html', {'title': 'Існуючий користувач', 'text': f'Привіт, {name}'})
