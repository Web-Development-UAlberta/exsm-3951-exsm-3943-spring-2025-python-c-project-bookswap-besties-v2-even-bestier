from django.db import models
from enum import Enum
from django.db import models
from authentication.models import Member

class ConditionType(Enum):
    new = "New"
    good = "Good"
    fair = "Fair"
    poor = "Poor"
   
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, to_field='member_id', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100, null=False)
    description = models.TextField()
    pub_date = models.DateField(null=False)
    condition = models.CharField(
      max_length=5,
      choices=ConditionType.choices, default=ConditionType.new, null=False
    )
    language = models.CharField(255)  
    price =  models.DecimalField(max_digits=6, decimal_places=2, null=False)
    weight = models.DecimalField(max_digits=7, decimal_places=3, null=False)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, to_field='member_id', on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    rating = models.IntegerField(default=0)
    review = models.TextField()

     def __str__(self):
        return f"{self.book.title}: {self.rating}"

class Wish_List(models.Model):
   id = models.AutoField(primary_key=True)
   book = models.ForeignKey(Book, to_field='book_id', on_delete=models.CASCADE, null=False)
   member = models.ForeignKey(Member, to_field='member_id', on_delete=models.CASCADE, null=False)

class Swap_Detail(models.Model):
   id = models.AutoField(primary_key=True)
   book = models.ForeignKey(Book, to_field='book_id' on_delete=models.CASCADE, null=False)
   original_owner_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
   new_owner_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
   swap_id = models.ForeignKey(Swap, on_delete=models.CASCADE, null=False)

class Sale(models.Model):
   id = models.AutoField(primary_key=True)
   seller_id = models.ForeignKey('Seller_Id',
        on_delete=models.CASCADE,
        null=False, db_column='seller_id',
        to_field='id')
   buyer_id = models.ForeignKey('Buyer_Id',
        on_delete=models.CASCADE,
        null=False, db_column='buyer_id',
        to_field='id')
   book = models.ForeignKey(Book, to_field='book_id', on_delete=models.CASCADE, null=False)
   shipment = models.ForeignKey(Shipment, to_field='shipement_id', on_delete=models.CASCADE, null=False)
   sale_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)

class Swap(models.Model):
   id = models.AutoField(primary_key=True)
   swap_date = models.DateField(null=False)

class Shipment(models.Model):
   id = models.AutoField(primary_key=True)
   shipment_date = models.DateField(null=False)
   address = models.CharField(max_length=255)
   shipment_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)
   
