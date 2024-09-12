from django.forms import ModelForm, widgets
from django import forms
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title"]
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"})}

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
