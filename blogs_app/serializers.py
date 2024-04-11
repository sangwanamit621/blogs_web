from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post,Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","email","first_name","last_name"]


class PostSerializer(serializers.ModelSerializer):  
    author_username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ["post_id","title","author","author_username","content","published_on","modified_on"]
        read_only_fields = ["published_on","modified_on","author"]

    def validate_author_username(self,value):
        try:
            user = User.objects.get(username=value)
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError(f"User {value} does not exists.")


    def create(self,validated_data):
        author_username = validated_data.pop("author_username")
        author = self.validate_author_username(author_username)
        validated_data["author"] = author
        return super().create(validated_data)
    
    def to_representation(self,instance):
        data = super().to_representation(instance)
        user_id = data["author"]
        user = User.objects.get(pk=user_id)
        data["author"] = user.username
        return data
    

class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    user_id = serializers.CharField(default=serializers.CurrentUserDefault())
    

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["published_on","modified_on","user_id"]

    


