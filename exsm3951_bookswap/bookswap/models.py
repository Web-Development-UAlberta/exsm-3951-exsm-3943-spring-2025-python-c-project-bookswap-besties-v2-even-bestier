from django.db import models
from enum import Enum
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from authentication.models import Member


class Book(models.Model):
    
    class BookCondition(models.TextChoices):
        new = "New"
        good = "Good"
        fair = "Fair"
        poor = "Poor"


    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    isbn = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100, null=False)
    description = models.TextField()
    pub_date = models.DateField(null=False)
    condition = models.CharField(
    max_length=4,
    choices=BookCondition.choices, default=BookCondition.new, null=False
    )
    language = models.CharField(max_length=100)  
    price =  models.DecimalField(max_digits=6, decimal_places=2, null=False)
    weight = models.DecimalField(max_digits=7, decimal_places=3, null=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False)
    review = models.TextField()

    def __str__(self):
        return f"{self.book.title}: {self.rating}"

"""
Many-to-many table 
A member can have many books on their wish list
A book can be part of many members' wish list
"""
class WishList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)


class Swap(models.Model):
    swap_date = models.DateField(null=False)


class Shipment(models.Model):
    shipment_date = models.DateField(null=False)
    address = models.CharField(max_length=255)
    shipment_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)


class SwapDetail(models.Model):
    swap = models.ForeignKey(Swap, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    original_owner = models.ForeignKey(Member, related_name="original_owner_swap_details", on_delete=models.CASCADE, null=False)
    new_owner = models.ForeignKey(Member, related_name="new_owner_swap_details", on_delete=models.CASCADE, null=False)
    # many swap details can belong to a single shipment
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=False)
   

class Sale(models.Model):
    seller = models.ForeignKey(Member, related_name="seller_sales", on_delete=models.CASCADE, null=False)
    buyer = models.ForeignKey(Member, related_name="buys_sales", on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=False)
    sale_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)
