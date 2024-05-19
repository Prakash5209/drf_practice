from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username','password',)


    def create(self,validated_data):
        user = get_user_model().objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
