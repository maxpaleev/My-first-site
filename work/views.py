import time

from django.shortcuts import render, redirect
from .models import Work
from .forms import WorkForm
from django.views.generic import DetailView, UpdateView, DeleteView

Today = time.localtime()


def work_home(request):
    work = Work.objects.all()
    return render(request, 'work/home.html', {'work': work})


class WorkDetail(DetailView):
    model = Work
    template_name = 'work/details.html'
    context_object_name = 'Work'


class WorkUpdate(UpdateView):
    model = Work
    template_name = 'work/create.html'

    form_class = WorkForm


class WorkDelete(DeleteView):
    model = Work
    success_url = '/homework'
    template_name = 'work/delete.html'


def work_create(request):
    error = ''
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_home')
        else:
            error = "Форма неверная"

    form = WorkForm()

    data = {
        'form': form,
        'error': error
    }
    if Today.tm_wday == 0:
        return render(request, 'work/create.html', data)
    elif Today.tm_wday == 1:
        return render(request, 'work/create1.html', data)
    elif Today.tm_wday == 2:
        return render(request, 'work/create2.html', data)
    elif Today.tm_wday == 3:
        return render(request, 'work/create3.html', data)
    elif Today.tm_wday == 4:
        return render(request, 'work/create4.html', data)
    elif Today.tm_wday == 5:
        return render(request, 'work/create5.html', data)
    else:
        return render(request, 'work/create.html', data)
