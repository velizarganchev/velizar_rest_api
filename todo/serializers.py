from django.contrib.auth.models import User # type: ignore
from rest_framework import serializers # type: ignore

from todo.models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',
                  'created_at', 'user', 'dateDiff']
