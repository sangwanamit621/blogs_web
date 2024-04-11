from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.format = 'json'
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = self.client.post(reverse('token_generate'), data={'username': 'testuser', 'password': 'testpassword'}, format=self.format).data['access']
        
            
    def test_register_user(self):
        data = {
            "username":"testuser2",
            "password":"testpassword2",
            "first_name":"Testing",
            "last_name":"User2",
            "email":"testuser2@gmail.com"
        }

        response = self.client.post(reverse('user_register'),data,format=self.format)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    

    def test_token_generate(self):
        data = {
            "username":"testuser",
            "password":"testpassword"
        }
        
        response = self.client.post(reverse('token_generate'),data=data,format=self.format)               
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_change_password(self):
        data = {
        "username":"testuser",
        "old_password":"testpassword",
        "new_password":"testpasswordupdated"
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        url = reverse('change_user_password',kwargs={'username':'testuser'})
        response = self.client.put(url,data,format=self.format)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_update_user_details(self):
        data = {
        "username":"test_user",
        "first_name":"Test User",
        "last_name":"Updated"
        }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        url = reverse('update_user_details',kwargs={'username':'testuser'})
        response = self.client.patch(url,data,format=self.format)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    

    


    
