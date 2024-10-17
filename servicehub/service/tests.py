from django.test import TestCase

# Create your tests here.

class TestArithmeticOperations(TestCase):
    def setUp(self):
        
        print('this is setup')
    @classmethod    
    def setUpTestData(cls):
        cls.num1 = 15
        cls.num2 = 12
        print('this is setup test data')


    def test_addition(self):
       
        result = self.num1 + self.num2
        # assert self.num1>0, 'number should be greater than zero'
        self.assertGreater(self.num1,0)
        self.assertEqual(result,27,'both are not same')
    def test_subtraction(self):
       
        result = self.num1 - self.num2
        self.assertEqual(result,3) 

    def tearDown(self):
        print('testing finished')   




        


