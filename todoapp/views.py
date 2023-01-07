from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoItemSerializer
from .models import TodoItem

# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all().order_by('todo')
    serializer_class = TodoItemSerializer