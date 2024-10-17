from django.test import TestCase

from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from django.db.utils import IntegrityError

from service.models import Customer

from django.utils import timezone

# class TestArithmeticOperations(TestCase):
#     def setUp(self):
        
#         print('this is setup')
#     @classmethod    
#     def setUpTestData(cls):
#         cls.num1 = 15
#         cls.num2 = 12
#         print('this is setup test data')


#     def test_addition(self):
       
#         result = self.num1 + self.num2
#         # assert self.num1>0, 'number should be greater than zero'
#         self.assertGreater(self.num1,0)
#         self.assertEqual(result,27,'both are not same')
#     def test_subtraction(self):
       
#         result = self.num1 - self.num2
#         self.assertEqual(result,3) 

#     def tearDown(self):
#         print('testing finished')
#         print('testing finishedfffffff')


class TestUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser',email='testuser@mailinator.com',password='testpassword')

    def test_create_user(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username,'testuser','username not same')
        self.assertEqual(user.email,'testuser@mailinator.com','mail not same')
        self.assertTrue(user.check_password('testpassword'))

    def test_string_representation(self):
        
        self.assertEqual(str(self.user),'testuser')

    def test_invalid_email(self):
        
        with self.assertRaises(ValidationError): 
            user = User.objects.create_user(username='testuser12',email='invalid-email',password='testpassword')
            user.full_clean()

    def test_duplicate_username(self):
        with self.assertRaises(IntegrityError):
            user = User.objects.create_user(username='testuser',email='testuser123@mailinator.com',password='testpassword') 


class TestCustomerModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser',password='testpassword')
        cls.customer = Customer.objects.create(name='testuser',
                                               phone='9847123123',
                                               email='testuser@mailinator.com',
                                               vehicle_number = 'abc123',
                                               running_kilometer = 2500,
                                               service_advisor = cls.user 

                                               )
    def test_create_customer(self):
        customer_obj = Customer.objects.get(id=1)
        self.assertEqual(Customer.objects.count(),1)
        self.assertTrue(isinstance(customer_obj,Customer))
        self.assertEqual(customer_obj.name,'testuser')
        self.assertEqual(customer_obj.phone,'9847123123')
        self.assertEqual(customer_obj.email,'testuser@mailinator.com')
        self.assertEqual(customer_obj.vehicle_number,'abc123')
        self.assertEqual(customer_obj.running_kilometer,2500)
        self.assertEqual(customer_obj.service_advisor,self.user)
        self.assertTrue(customer_obj.is_active)

    def test_invalid_phone_number(self):
        
        self.customer = Customer.objects.create(name='testcustomer',
                                               phone='9847',
                                               email='testuser@mailinator.com',
                                               vehicle_number = 'abc123',
                                               running_kilometer = 2500,
                                               service_advisor = self.user 

                                   )
        with self.assertRaises(ValidationError):
            self.customer.full_clean()

    def test_string_representaion(self):
        self.assertEqual(str(self.customer),'testuser')

    def test_created_date(self):
        # print(timezone.now())
        self.assertIsNotNone(self.customer.created_date)  
        self.assertLessEqual(self.customer.created_date,timezone.now())
    def test_updated_date(self):
        customer = Customer.objects.create(name='testuser123',
                                               phone='9847123123',
                                               email='testuser@mailinator.com',
                                               vehicle_number = 'abc123',
                                               running_kilometer = 2500,
                                               service_advisor = self.user 

                                               )
        customer.vehicle_number ='abcd1234'
        customer.save()

        self.assertIsNotNone(customer.updated_date)
        self.assertLessEqual(customer.updated_date,timezone.now())
        self.assertGreaterEqual(customer.updated_date,customer.created_date)

    def test_work_status(self):
        self.assertIsNotNone(self.customer.work_status)
        self.assertEqual(self.customer.work_status,'pending') 
        self.assertIn(self.customer.work_status,dict(Customer.work_status_choices).keys())
    def test_invalid_work_status(self):
        with self.assertRaises(ValidationError):
            customer = Customer.objects.create(name='testuser123',
                                               phone='9847123123',
                                               email='testuser@mailinator.com',
                                               vehicle_number = 'abc123',
                                               running_kilometer = 2500,
                                               service_advisor = self.user,
                                               work_status='Invalid Status' 


                                               )

         
            customer.full_clean()
          

    def test_name_exeeds_max_length(self):
        cust_name = 'testuser'*200
        
        customer = Customer.objects.create(name=cust_name,
                                               phone='9847123123',
                                               email='testuser@mailinator.com',
                                               vehicle_number = 'abc123',
                                               running_kilometer = 2500,
                                               service_advisor = self.user 


                                               )
        with self.assertRaises(ValidationError):
            customer.full_clean()

    def test_running_kilometer(self):

        with self.assertRaises(IntegrityError):
            Customer.objects.create(name='testuser123',
                                                phone='9847123123',
                                                email='testuser@mailinator.com',
                                                vehicle_number = 'abc123',
                                                running_kilometer = -2500,
                                                service_advisor = self.user,
                                                


                                                )
        



            


             






              

           









        


