from rest_framework import viewsets,status,serializers
from .models import User
from .serializers import RegistrationSerializer,LoginSerializer
from utils.functions import generate_user_id
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from rest_framework.exceptions import MethodNotAllowed
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationViewset(viewsets.ModelViewSet):
    serializer_class=RegistrationSerializer
    queryset=User.objects.all()
    def create(self,request:Request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        try:
            
            if serializer.is_valid():
                serializer.validated_data['id']=generate_user_id()
                serializer.save()
                return Response(
                    data={
                        "success":"Account created successfully"
                    },
                    status=status.HTTP_201_CREATED
                )
                
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
        except serializers.ValidationError as e:
            return Response({'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrive(self, request, *args, **kwargs):
        return MethodNotAllowed('GET')
    
    def update(self, request, *args, **kwargs):
        return MethodNotAllowed('PUT')
    
    def delete(self, request, *args, **kwargs):
        return MethodNotAllowed('DELETE')
class LoginViewset(viewsets.ModelViewSet):
    serializer_class=LoginSerializer
    queryset=User.objects.all()
    
    def create(self, request:Request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data.get("email") 
            password=serializer.validated_data.get("password")
            user=authenticate(email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },status=status.HTTP_200_OK)
                
            return Response(
                data="Account login failed",
                status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data="Invalid data provided",
            status=status.HTTP_400_BAD_REQUEST
        )
    
    