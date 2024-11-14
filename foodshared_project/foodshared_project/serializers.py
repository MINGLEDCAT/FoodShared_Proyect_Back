from rest_framework import serializers
from .models import Alimentos

class AlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'
