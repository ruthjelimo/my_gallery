from django.test import TestCase
from .models import Author,Image,Location

# Create your tests here.
class AuthorTestClass(TestCase):

    # Set up method
    def setUp(self):
        
        self.Kimberly=Author(first_name = 'Kimberly',last_name = 'Kardashian',email='kimkay@gmail.com',phone_number='0712437151')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Kimberly,Author))

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(id=1,location_name = 'Embakasi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

           # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
# Testing delete Method
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)== 0) 
        # Testing update location Method


