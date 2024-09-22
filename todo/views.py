from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from rest_framework import permissions, viewsets # type: ignore
from django.core import serializers # type: ignore

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(title=request.POST.get('title', ""),
                                   description=request.POST.get(
                                       'description', ""),
                                   user=request.user,
                                   )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')
