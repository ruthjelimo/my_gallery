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
    pub_date = models.DateTimeField(auto_now_add=True)
   
    # location = models.ForeignKey('Location', on_delete = models.CASCADE)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)


    def save_image(self):
        self.save()                    
    
    def delete_image(self):
        self.delete()
  
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_one_image(cls,id):
        images = cls.objects.filter(id = id)
        return Image

    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image

    
    @classmethod
    def view_images_by_location(cls,location):
        location_images = cls.objects.filter(location= location)

        return location_images

    @classmethod
    def view_images_by_category(cls,category):
        category = cls.objects.filter(category = category)
        return category

    

   

