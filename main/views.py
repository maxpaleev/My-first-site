from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    data = {
        'title': 'Главная страница',
        #  список данных
        # 'values': ['Some', 'Hello', '123'],
        # 'obj': {
        #     'car': 'BMW',
        #     'age': 18,
        #     'hobby': 'Football'
        # }
    }

    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")


def author(request):
    return render(request, "main/author.html")


def contacts(request):
    return render(request, 'main/contacts.html')
