from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


class User(AbstractUser):
    pass


class Auctions(models.Model):
    CATEGORY_CHOICES = [
        (None, 'Select'),
        ('fashion', 'Fashion'),
        ('electornics', 'Electornics'),
        ('furniture', 'Furniture'),
        ('toys', 'Toys'),
        ('books', 'Books'),
        ('kitchen', 'Kitchen'),
        ('others', 'Others')
    ]
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    starting_price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='Select')
    username = models.CharField(max_length=16)

    def __str__(self):
        return self.title
    

class AuctionsForm(ModelForm):
    class Meta:
        model = Auctions
        fields = ['title', 'description', 'starting_price', 'image_url', 'category', 'username']


class Bids(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=16)
    bids = models.IntegerField(max_length=3)


class Comments(models.Model):
    pass