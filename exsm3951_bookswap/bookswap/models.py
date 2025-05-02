from django.db import models
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


class Shipment(models.Model):
    shipper = models.ForeignKey(Member, related_name="shipper_shipment", on_delete=models.CASCADE, null=False)
    recipient = models.ForeignKey(Member, related_name="recipient_shipment", on_delete=models.CASCADE, null=False)
    shipment_date = models.DateField(null=False)
    shipment_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    
    # derived properties
    @property
    def shipper_address(self):
        return self.shipper.address
    
    @property
    def recipient_address(self):
        return self.recipient.address
    
    
       
class Swap(models.Model):
    pass  # will still get the id field from django
    
    
class Transaction(models.Model):
    
    class TransactionType(models.TextChoices):
        sale = "Sale"
        swap = "Swap"
        
        
    transaction_type = models.CharField(max_length=4, choices=TransactionType.choices, null=False)
    transaction_date = models.DateField(null=False)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    from_member = models.ForeignKey(Member, related_name="from_member", on_delete=models.CASCADE, null=False)
    to_member = models.ForeignKey(Member, related_name="to_member", on_delete=models.CASCADE, null=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    swap = models.ForeignKey(Swap, on_delete=models.CASCADE, null=True)  # null when transaction_type is Sale
