from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
class WorkViewset(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
class WorkerViewset(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer