from django.test import TestCase
from .models import Author,Image

# Create your tests here.
class AuthorTestClass(TestCase):

    # Set up method
    def setUp(self):
        
        self.Kimberly=Author(first_name = 'Kimberly',last_name = 'Kardashian',email='kimkay@gmail.com',phone_number='0712437151')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Kimberly,Author))


