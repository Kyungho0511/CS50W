from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from django import forms
from decimal import Decimal


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
    current_price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal("0.00"))
    image_url = models.URLField()
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='Select')
    username = models.CharField(max_length=16)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class AuctionsForm(ModelForm):
    class Meta:
        model = Auctions
        fields = ['title', 'description', 'starting_price', 'current_price',
                  'image_url', 'category', 'username', 'closed']
        widgets = {
            'closed': forms.HiddenInput(), 
            'current_price': forms.HiddenInput(),
            'username': forms.HiddenInput()
            }


class Bids(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    winner = models.CharField(max_length=16)
    bids = models.IntegerField()
    closed = models.BooleanField(default=False)


class BidsForm(ModelForm):
    class Meta:
        model = Bids
        fields = ['title', 'price', 'winner', 'bids', 'closed']
        widgets = {
            'title': forms.HiddenInput(),
            'winner': forms.HiddenInput(),
            'bids': forms.HiddenInput(),
            'closed': forms.HiddenInput(),
            'price': forms.NumberInput(attrs={'placeholder': 'Bid', 'autofocus': True})
        }
        labels = {'price': ""}


class Comments(models.Model):
    auction_id = models.ForeignKey(Auctions, on_delete=models.CASCADE, db_column="auction_id")
    username = models.CharField(max_length=16)
    contents = models.TextField(max_length=1000)

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['auction_id', 'username', 'contents']
        widgets = {
            'auction_id': forms.HiddenInput(),
            'username': forms.HiddenInput(),
            'contents': forms.TextInput(attrs={'placeholder': 'Add a comment...', 'autocomplete': 'off'})
        }
        labels = {'contents': ""}