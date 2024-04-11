from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, RegisterUserSerializer, ChangePasswordSerializer, UpdateUserDetailSerializer



class MyTokenObtainPairViewSet(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class RegisterUserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterUserSerializer


class ChangePasswordViewSet(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    lookup_field = "username"


    def update(self, request,*args,**kwargs):
       instance = self.get_object()

       serializer = self.get_serializer(instance, data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)

       result = {
        "message": "success",
        "details": f"Successfully changes password for {serializer.data['username']} !!!",
        "status": 200,
       }

       return Response(result)



class UpdateUserDetailsViewSet(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserDetailSerializer
    lookup_field = "username"


    def update(self,request,*args,**kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        result = {
        "message": "success",
        "updated_details":serializer.data,
        "status": 200,  }

        return Response(result)