from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from rest_framework import routers # type: ignore

from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
