from django.forms import widgets
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "temps/index.html")

def tasks(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "temps/tasks.html", {"tasks": request.session["tasks"],})

class taskForm(forms.Form):
    tasks = forms.CharField(label="Enter Your Task ", widget=forms.TextInput(attrs={"class": "taskInput", "id": "taskIn"}))

def add(request):
    if request.method == "POST":
        form = taskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("tasks:task" ))
    return render(request, "temps/add.html", {"form": taskForm()})