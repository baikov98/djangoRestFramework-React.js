from .models import Todo
from rest_framework import viewsets, permitions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permitions_classes = [
        permitions.AllowAny
    ]
    seriaizer_class = TodoSerializer