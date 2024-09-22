from django.contrib import admin # type: ignore
from todo.models import Todo

admin.site.register(Todo)
