from django.db import models

# Create your models here.

class Drawings(models.Model):
    image = models.ImageField(upload_to='drawings/')
    year = models.PositiveBigIntegerField()
    Commissioned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['year', 'created_at']

    def __str__(self):
        return f"{self.image} ({self.year})"

class ExhibitedWorks(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField(max_length=10)
    availability = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title

class PriceList(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=10)

    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    size = models.CharField(max_length=200)
    style = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    Frame = models.BooleanField()

    def __str__(self):
        return self.style

class ContactInfo(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)  
    message = models.TextField(max_length=1000)
    