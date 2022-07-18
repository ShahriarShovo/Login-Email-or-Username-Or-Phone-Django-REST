from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.hashers import make_password


class User_Serializers(serializers.ModelSerializer):


    # check the new save method
    def create(self,validated_data):
        obj = self.Meta.model(**validated_data)
        password = validated_data['password']

        if password is not None:
            obj.password = make_password(password)
            obj.save()
            print('save')

            return obj


    class Meta:
        model=User
        fields=['email', 'phone', 'username', 'password']

       





