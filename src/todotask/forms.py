from django import forms
from .models import Todo

DEPARTAMENT = [
    ("Inginerie", "Inginerie"),
    ("HR", "Human Resource"),
    ("Sales", "Sales"),
    ("Management", "Management"),
]

STATUS = [
    ("WIP", "WIP"),
    ("DONE", "DONE"),
]

# class DepartamentForm(forms.Form):
#     title = forms.CharField(label='Title', max_length=100)
#     task = forms.CharField(label= 'Task', max_length=1000, widget=forms.Textarea())
#     departament = forms.ChoiceField(label='Departament', choices=DEPARTAMENT)

class DepartamentForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", 'status', "task", "departament"]