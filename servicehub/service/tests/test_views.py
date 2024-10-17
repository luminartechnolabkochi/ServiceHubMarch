from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from django.urls import reverse

from service.models import Customer



class TestCustomerListCreateView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # cls.user = User.objects.create_user(username='testuser',password='testpassword')
        cls.admin = User.objects.create_superuser(username='testadmin',password='testpassword')
        cls.url = '/api/customers/'
        # cls.url = reverse('')

        cls.admin_token = Token.objects.create(user=cls.admin)

    def test_customer_create_view(self):
        # self.client.force_login(self.admin)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token}')
        
        data={
    
                    "name": "testcustomer",
                    "phone": "919961980428",
                    "email": "sarathkv8895@gmail.com",
                    "vehicle_number": "kl-59-u-6865",
                    "running_kilometer": 49000
            }
        self.response=self.client.post(self.url,data)
        print(self.response)

        self.assertEqual(self.response.status_code,201) 
        self.assertEqual(self.response.data.get('name'),'testcustomer')
        


