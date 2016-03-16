from rest_framework import generics

from .models import Task
from .serializer import TaskSerializer


class ToDoListCreateViewAPI(generics.ListCreateAPIView):
    """Todo create and list endpoint"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ToDoRetrieveUpdateDestroyViewAPI(generics.RetrieveUpdateDestroyAPIView):
    """Todo retrieve update delete"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

