from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
class WorkViewset(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
class WorkerViewset(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
class AnotherViewset(ModelViewSet):
    queryset = Another.objects.all()
    serializer_class = AnotherSerializer