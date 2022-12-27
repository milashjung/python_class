from django.shortcuts import render
from django.urls import reverse
from todofeature.models import Task
from todofeature.forms import TaskForm
from django.http import HttpResponseRedirect


def todo_list_view(request):
    return render(request, "todo_list.html")



def todo_add_view(request):
   form = TaskForm(request.POST or None)
   if form.is_valid():
    # print(form.cleaned_data)]
    form.save()
    return HttpResponseRedirect(reverse("todofeature:todo_list"))
   return render(request, "add_todo.html",{"form": form})
 