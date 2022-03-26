from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.first_name


class Image(models.Model):
    image = models.ImageField(upload_to= 'images/')
    description = models.CharField(max_length=50)
    name = models.CharField(max_length=55)    
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)

   

