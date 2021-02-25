from rest_framework import serializers
from .models import ConstrProjModel


class ConstrProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstrProjModel
        fields = '__all__'
