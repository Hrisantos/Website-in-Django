from django.shortcuts import render, redirect
##
from .models import Todo
from .forms import DepartamentForm
## import filter
from .filters import TodoFilter
# Create your views here.

def todo_screen_view(request):
    if request.method == 'POST':
        form = DepartamentForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = DepartamentForm()
            departament = Todo.objects.all()

            myFilter = TodoFilter(request.GET, queryset=departament)
            departament = myFilter.qs

            context = {'form': form, 'todo': departament, 'myFilter': myFilter}
            return render(request, "todotask/todotask.html", context)
    else:
        form = DepartamentForm()
        departament = Todo.objects.all()

        myFilter = TodoFilter(request.GET, queryset=departament)
        departament = myFilter.qs

        context = {'form': form, 'todo': departament, 'myFilter': myFilter}

        return render(request, "todotask/todotask.html", context)

def delete(request, id):
    departament = Todo.objects.get(pk=id)
    departament.delete()
    return redirect("todo")

def change_status_na(request, id):
    departament = Todo.objects.get(pk=id)
    if departament.status == "N/A":
        departament.status = "WIP"
        departament.save()
    else:
        departament.status = "N/A"
    return redirect("todo")

def change_status_wip(request, id):
    departament = Todo.objects.get(pk=id)
    if departament.status == "WIP":
        departament.status = "DONE"
        departament.save()
    else:
        departament.status = "DONE"
    return redirect("todo")

def change_status_done(request, id):
    departament = Todo.objects.get(pk=id)
    if departament.status == "DONE":
        departament.status = "N/A"
        departament.save()
    else:
        departament.status = "DONE"
    return redirect("todo")
