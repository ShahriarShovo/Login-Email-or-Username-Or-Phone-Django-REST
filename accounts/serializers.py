from rest_framework import serializers
from accounts.models import User


class User_Serializers(serializers.ModelSerializer):

    password = serializers.CharField(max_length=255,style={'input_type':'password'})


    class Meta:
        model=User
        fields=['email', 'phone', 'username', 'password']

        # def create(self, validated_data):
        #     password = validated_data.pop('password', None)
        #     instance = self.Meta.model(**validated_data)
        #     if password is not None:
        #         instance.set_password(password)
        #     instance.save()
        #     return instance

