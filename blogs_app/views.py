from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.pagination import PageNumberPagination
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("post_id")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination


    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        author = serializer.validated_data.get("author_username")
        
        if user != author:
            error_message = {
                "status":status.HTTP_403_FORBIDDEN,
                "message":"You are not allowed to create a post on the behalf of another user."
            }
            return Response(error_message,status=status.HTTP_403_FORBIDDEN)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = {
            "status": status.HTTP_201_CREATED,
            "message": "Post created successfully",
            "data": serializer.data
        }
        return Response(response,status=status.HTTP_201_CREATED, headers=headers)
    

    def update(self,request,*args,**kwargs):
        partial = kwargs.pop("partial",False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        author = instance.author
        user = request.user

        if user!=author:
            error_message = {
                "status":status.HTTP_403_FORBIDDEN,
                "message":"You are not allowed to update the post of other user."
            }
            return Response(error_message,status=status.HTTP_403_FORBIDDEN)
        
        self.perform_update(serializer)

        response = {
            "status": status.HTTP_200_OK,
            "message": "Post updated successfully",
            "data": serializer.data
        }
        return Response(response,status=status.HTTP_200_OK)
    

    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        author = instance.author
        user = request.user

        if user!=author:
            error_message = {
                "status":status.HTTP_403_FORBIDDEN,
                "message":"You are not allowed to delete a post of other user."
            }
            return Response(error_message,status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(instance)
        
        response = {
            "status": status.HTTP_200_OK,
            "message": "Post deleted successfully"
        }
        return Response(response,status=status.HTTP_200_OK)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("post_id")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def update(self,request,*args,**kwargs):
        partial = kwargs.pop("partial",False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=partial)
        serializer.is_valid(raise_exception=True)

        user = request.user
        commenter = serializer.validated_data.get("user_id")
        commenter = instance.user_id
              
        if user!=commenter:
            error_message = {
                "status":status.HTTP_403_FORBIDDEN,
                "message": "You are not allowed to modify the comment of other user."
            }

            return Response(error_message,status=status.HTTP_403_FORBIDDEN)
        
        self.perform_update(serializer)

        response = {
            "status":status.HTTP_200_OK,
            "message":"Comment updated successfully",
            "data":serializer.data
        }
        return Response(response,status=status.HTTP_200_OK)
    
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        commentor = instance.user_id
        user = request.user

        if user!=commentor:
            error_message = {
                "status":status.HTTP_403_FORBIDDEN,
                "message":"You are not allowed to delete comment of other user."
            }
            return Response(error_message,status=status.HTTP_403_FORBIDDEN)
        
        response = {
            "status":status.HTTP_200_OK,
            "message":"Comment deleted successfully"
        }
        return Response(response,status=status.HTTP_200_OK)
    

    


    