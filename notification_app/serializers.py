from rest_framework import serializers
from .models import *

class RegisteredAndroidUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredAndroidUser
        # exclude = ('id',)
        # fields = '__all__'
        fields = ['mobile', 'name', 'fcm_token']
