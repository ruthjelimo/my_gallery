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
    location = models.ForeignKey('Location', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
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
    def search_images_by_location(cls,location):
        location_images = cls.objects.filter(location__location_name= location)

        return location_images

    @classmethod
    def search_images_by_category(cls,category):
        category = cls.objects.filter(category__category_name= category)
        return category


    def __str__(self):
        return self.name

    

class Category(models.Model):
    category_name = models.CharField(max_length=60)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

        
    @classmethod
    def get_categories(cls):
        categories = cls.objects.all()

        return categories

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length=70)

    def save_location(self):
        self.save()


    def delete_location(self):
        self.delete()
        
    

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.location_name 


