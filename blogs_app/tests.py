from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


class PostAPITestCase(TestCase):

    def setUp(self):
        self.client=APIClient()
        self.format='json'
        self.user = User.objects.create_user(username='testuser',password='testpassword')
        self.token = self.client.post(reverse('users-auth:token_generate'),data={'username': 'testuser', 'password': 'testpassword'}, format=self.format).data['access']
        

    def create_post(self):
        data = {
            "title":"Test Post",
            "content":"This is the test post"
        }

        url = reverse('blogs-app:post-ops-list')
        self.client.credentials(HTTP_AUTHORIZATION=F'Bearer {self.token}')
        response = self.client.post(url,data=data,format=self.format)   
        return response

        
    def test_add_post(self):
        response = self.create_post()        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)  


    def test_modify_post(self):
        data = {
            "title":"First Post title is modified",
            "content":"This is first modified post"
        }

        response = self.create_post()        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)        
        post_id = response.data['data']['post_id']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('blogs-app:post-ops-detail',kwargs={'pk':post_id})
        response = self.client.patch(url,data,format=self.format)
          
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_retrieve_post(self):
        response = self.create_post()
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('blogs-app:post-ops-list')
        response = self.client.get(url,format=self.format)
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_remove_post(self):
        data = {
            "title":"First Post",
            "content":"This is first post"
        }

        response = self.create_post()        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)        
        post_id = response.data['data']['post_id']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        url = reverse('blogs-app:post-ops-detail',kwargs={'pk':post_id})
        response = self.client.delete(url,data,format=self.format)          
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        url = reverse('blogs-app:post-ops-detail',kwargs={'pk':post_id})
        response = self.client.delete(url,data,format=self.format)          
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    
class CommentAPITestCase(TestCase):

    def setUp(self):
        self.client=APIClient()
        self.format='json'
        self.user = User.objects.create_user(username='testuser',password='testpassword')
        self.token = self.client.post(reverse('users-auth:token_generate'),data={'username': 'testuser', 'password': 'testpassword'}, format=self.format).data['access']
        

    def create_post(self):
        data = {
            "title":"Test Post",
            "content":"This is the test post"
        }

        url = reverse('blogs-app:post-ops-list')
        self.client.credentials(HTTP_AUTHORIZATION=F'Bearer {self.token}')
        response = self.client.post(url,data=data,format=self.format)   
        return response
    

    def add_comment(self):
        response = self.create_post()        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)        
        post_id = response.data['data']['post_id']

        data = {
            "comment":"This is a test comment on post",
            "post_id":post_id
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('blogs-app:comment-ops-list')
        response = self.client.post(url,data,format=self.format)
        return response


    def test_add_comment(self):        
        response = self.add_comment()        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)  


    def test_modify_comment(self):

        response = self.add_comment()        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)    
        comment_id = response.data['comment_id']

        data = {
            "comment":"This is a test comment on post to update the comment"
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('blogs-app:comment-ops-detail',kwargs={'pk':comment_id})
        response = self.client.patch(url,data,format=self.format)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        

    def test_retrieve_comment(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('blogs-app:comment-ops-list')
        response = self.client.get(url,format=self.format)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        