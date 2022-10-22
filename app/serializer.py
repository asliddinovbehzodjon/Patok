from rest_framework import serializers
from .models import *
class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
class AnotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Another
        fields = "__all__"