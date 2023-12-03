from django.db import models

# Create your models here.

DEPARTAMENT = [
    ("Inginerie", "Inginerie"),
    ("HR", "Human Resource"),
    ("Sales", "Sales"),
    ("Management", "Management"),
]

STATUS = [
    ("N/A", "N/A"),
    ("WIP", "WIP"),
    ("DONE", "DONE"),
]

class Todo(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS, blank=True)
    task = models.TextField(max_length=1000)
    date_creation = models.DateTimeField(verbose_name="Task creation", auto_now_add=True)
    departament = models.CharField(max_length=50, choices=DEPARTAMENT)

    def __str__(self):
        return self.title + " ------> Departament: " + self.departament

    class Meta:
        # verbose_name = variabila pentru a schimba denumirea in admin panel
        # verbose_name_plural = variabila pentru a schimba denumirea in admin panel
        pass
