from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    class Meta:
        fields = ["username","password"]


    @classmethod
    def get_token(cls,user):
        token = super(MyTokenObtainPairSerializer,cls).get_token(user)

        token["username"] = user.username
        return token


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators= [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


    class Meta:
        model = User
        fields = ["username","password","email","first_name","last_name"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True}
        }


    def create(self,validate_data):
        user = User.objects.create(
            username=validate_data["username"],
            email = validate_data["email"],
            first_name = validate_data["first_name"],
            last_name = validate_data["last_name"]
        )

        user.set_password(validate_data["password"])
        user.save()

        return user
    

class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    old_password = serializers.CharField(write_only=True,required=True)
    username = serializers.CharField(required=True)


    class Meta:
        model = User
        fields = ["username","old_password","new_password"]


    def validate(self, attrs):
        if attrs["new_password"]==attrs["old_password"]:
            raise serializers.ValidationError({"password": "Old and New Passwords are same. Please pass other value in new password."})
        
        return attrs
    
    
    def validate_old_password(self,value):
        user = self.context["request"].user
        
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password":"Old password is not correct"})
        
        return value
    

    def update(self,instance,validated_data):
        user = self.context["request"].user

        if user.pk!=instance.pk:
            raise serializers.ValidationError({"authorize":"You dont have the permissions to change password of this user"})
        
        instance.set_password(validated_data["new_password"])
        instance.save()
        
        return instance
        

class UpdateUserDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)


    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        extra_kwargs = {
            "first_name": {"required":False},
            "last_name": {"required":False}
        }


    def validate_email(self,value):
        user = self.context["request"].user

        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email":"This email is already in use"})
        
        return value
    
    
    def update(self,instance,validated_data):
        user = self.context["request"].user

        if user.pk!=instance.pk:
            raise serializers.ValidationError({"authorize":"You dont have the permission to update details of this user"})
        
        if validated_data.get("first_ name"):
            instance.first_name = validated_data["first_name"]
        if validated_data.get("last_name"):
            instance.last_name = validated_data["last_name"]
        if validated_data.get("email"):
            instance.email = validated_data["email"]
        if validated_data.get("username"):
            instance.username = validated_data["username"]

        instance.save()

        return instance