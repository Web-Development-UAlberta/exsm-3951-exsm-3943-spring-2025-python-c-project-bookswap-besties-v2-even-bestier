from django.test import TestCase
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction
from authentication.models import Member

#sources: https://docs.djangoproject.com/en/5.2/topics/testing/overview/

class MemberModelTests(TestCase):
    def test_create_member(self):
        member = Member.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            password='password123'
        )
        self.assertEqual(member.email, 'johndoe@example.com')
        self.assertEqual(member.first_name, 'John')
        self.assertEqual(member.last_name, 'Doe')

class BookModelTests(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            isbn='1234567890',
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            genre='Fiction',
            description='A classic novel',
            pub_date='1954-09-25',
            language='English',
            weight=4.5
        )
        self.assertEqual(book.title, 'The Great Gatsby')
        self.assertEqual(book.isbn, '1234567890')
        self.assertEqual(book.author, 'F. Scott Fitzgerald')
        self.assertEqual(book.weight, 4.5)

class BookListingModelTests(TestCase):
    def test_create_booklisting(self):
        member = Member.objects.create(
            first_name='Alice',
            last_name='Smith',
            email='alice@example.com',
            password='password123'
        )

        book = Book.objects.create(
            isbn='9876543210',
            title='1984',
            author='George Orwell',
            genre='Dystopian',
            description='A novel about surveillance and control',
            pub_date='1949-06-08',
            language='English',
            weight=4.0
        )
        
        listing = BookListing.objects.create(
            book=book,
            member_owner=member,
            condition='Good',
            price=12.50
        )
        self.assertEqual(listing.condition, 'Good')
        self.assertEqual(listing.price, 12.50)
        self.assertEqual(listing.book.title, '1984')
        self.assertEqual(listing.member_owner.email, 'alice@example.com')



""" This won't run until we have views and templates
class BookViewTests(TestCase):
    def test_book_listing_view(self):
        member = Member.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.com',
            password='password123'
        )
        book = Book.objects.create(
            isbn='1234567890',
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            genre='Fiction',
            description='A classic novel',
            pub_date='1954-09-25',
            language='English',
            weight=4.5
        )
        
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Great Gatsby')
"""