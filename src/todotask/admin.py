from django.contrib import admin
##
from todotask.models import Todo
# Register your models here.

# Cum sa creezi un search field
class AdminTodo(admin.ModelAdmin):
    list_display = ("title", "task", "departament")
    search_fields = ("title", "departament")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Todo, AdminTodo)