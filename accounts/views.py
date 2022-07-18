from django.shortcuts import render
from rest_framework.decorators import api_view
from accounts.models import User
from accounts.EmailBackend import EmailBackend
from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import User_Serializers
from django.contrib.auth.hashers import make_password

# Create your views here.


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def user_registration(request):
    if request.method=='POST':
        password=request.data.get('password')
        user=User_Serializers(data=request.data)
        if user.is_valid():
            #user_serialiers.set_password(password)
            #user.password = make_password('password')
            user.save()
            #user.set_password(user_serialiers[password])
            #token = get_tokens_for_user(user)
            return Response({'message':'you siginup in Successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(user.errors, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message':'Something wrong ! Try again'}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def user_login(request):
    if request.method=='POST':
        user=authenticate(request, username=request.POST.get('uep'), password=request.POST.get('password'))
        if user is not None:
            token = get_tokens_for_user(user)
            #login(request,user)
            return Response({'message':'you are logged in Successfully','token':token}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Your Crediential is not Correct'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message':'Something wrong ! Try again'}, status=status.HTTP_400_BAD_REQUEST)

