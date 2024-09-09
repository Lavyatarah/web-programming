from django import forms
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Define a new form for tasks
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")  # Corrected: CharField, not charfield
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# View for the index page
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, 'tasks/index.html', {
        "tasks": request.session["tasks"]
    })

# View for adding a new task
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
    else:
        form = NewTaskForm()

    return render(request, "tasks/add.html", {
        "form": form
    })
