from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()
from rest_framework.views import APIView
from rest_framework import permissions
# Create your views here.


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
    
        email = data['email']
        name = data['name']
        password = data['password']
        password2 = data['confirm paswords']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response('user already exists')
            else:
                if len(password) < 6:
                    return Response({'error':'Password must be more than 6 characters'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({'success':f'Account successfully created for {email}'})
        else:
            return Response({'error':'password not matched'})
                    