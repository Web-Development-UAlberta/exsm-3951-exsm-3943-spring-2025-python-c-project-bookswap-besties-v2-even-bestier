from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from authentication.models import Member
from django.utils import timezone
from django.core.exceptions import ValidationError
from decimal import Decimal 


def validate_not_future_date(value):
    if value > timezone.now().date():
        raise ValidationError("Publication Date cannot be in the future")

def validate_shipment_date(value):
    if value < timezone.now().date():
        raise ValidationError("Shipment cannot be in the past")
    
    
isbn_validator = RegexValidator(
    regex=r'^(?:\d{9}[\dXx]|\d{13})$',
    message="Enter a valid ISBN-10 or ISBN-13 number without dashes."
)

class Book(models.Model):
    class Language(models.TextChoices):
        english = 'en', 'English'
        french = 'fr', 'French'
        
    isbn = models.CharField(max_length=100, null=False, unique=True, db_index=True, validators=[isbn_validator])
    title = models.CharField(max_length=100, null=False, db_index=True)
    author = models.CharField(max_length=100, null=False, db_index=True)
    genre = models.CharField(max_length=100, null=False)
    description = models.TextField()
    pub_date = models.DateField(null=False, validators=[validate_not_future_date])
    language = models.CharField(max_length=100, choices=Language.choices, default=Language.english, null=False)  
    weight = models.DecimalField(max_digits=7, decimal_places=2, default=0.1, null=False)
    image_url = models.TextField(default="No image", null=False)

    def __str__(self):
        return self.title
    
class LibraryItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.book.title}"    


class BookListing(models.Model):
    
    class BookCondition(models.TextChoices):
        new = "New"
        good = "Good"
        fair = "Fair"
        poor = "Poor"
        
    library_item = models.ForeignKey(LibraryItem, on_delete=models.CASCADE, null=True)
    member_owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, related_name='book_listings')
    condition = models.CharField(
        max_length=4,
        choices=BookCondition.choices, default=BookCondition.new, null=False
    )
    price =  models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))], null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False, null=False)
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    review = models.TextField()
    
    create_at = models.DateTimeField(auto_now_add=True)

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

    #make sure the combination of member and book is unique
    class Meta:
        unique_together = ('member', 'book')
        

class Swap(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    

class Shipment(models.Model):
    shipment_date = models.DateField(null=False, validators=[validate_shipment_date])
    shipment_cost = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.00)], null=False)
    weight = models.DecimalField(max_digits=7, decimal_places=3, default=0.01, validators=[MinValueValidator(0.01)], null=False)
    address = models.TextField(max_length=255, blank=False, null=False)
    
    
class Transaction(models.Model):
    
    class TransactionType(models.TextChoices):
        sale = "Sale"
        swap = "Swap"
        
    class TransactionStatus(models.TextChoices):
        pending = "Pending"
        accepted = "Accepted"
        rejected = "Rejected"
        
        
    transaction_type = models.CharField(max_length=4, choices=TransactionType.choices, null=False)
    transaction_status = models.CharField(max_length=8, choices=TransactionStatus.choices, default=TransactionStatus.pending, null=False)
    transaction_date = models.DateField(auto_now_add=True, null=False)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=False)
    book_listing = models.ForeignKey(BookListing, on_delete=models.CASCADE, null=False)
    from_member = models.ForeignKey(Member, related_name="from_member", on_delete=models.CASCADE, null=False)
    to_member = models.ForeignKey(Member, related_name="to_member", on_delete=models.CASCADE, null=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False,  default=Decimal("0.00"))
    swap = models.ForeignKey('Swap', on_delete=models.CASCADE, null=True, blank=True)  # keep track of swaps
    

    def clean(self):
        super().clean()
        if self.from_member == self.to_member:
            raise ValidationError("A member cannot sell/swap with themselves")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        