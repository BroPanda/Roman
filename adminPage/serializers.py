from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ConstrProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
