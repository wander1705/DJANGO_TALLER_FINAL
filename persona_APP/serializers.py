from rest_framework import serializers
from .models import Proyecto

class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'