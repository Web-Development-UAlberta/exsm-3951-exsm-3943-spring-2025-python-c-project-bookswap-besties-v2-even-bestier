from django.test import TestCase
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction
from authentication.models import Member

#sources: https://docs.djangoproject.com/en/5.2/topics/testing/overview/

class MemberModelTests(TestCase):
    def test_create_member(self):
        member = Member.objects.create(
            username='jdoe',
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
            username='asmith',
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

class ReviewModelTests(TestCase):
    def test_create_review(self):
        member = Member.objects.create(
            username='bmarley',
            first_name='Bob',
            last_name='Marley',
            email='bobm@example.com',
            password='password123'
        )

        book = Book.objects.create(
            isbn='1111111111',
            title='Brave New World',
            author='Aldous Huxley',
            genre='Science Fiction',
            description='A dystopian novel',
            pub_date='1932-01-01',
            language='English',
            weight=3.0
        )

        review = Review.objects.create(
            book=book,
            member=member,
            rating=5,
            review='A fascinating and eerie read!'
        )

        self.assertEqual(review.rating, 5)
        self.assertIn('fascinating', review.review)
        self.assertEqual(review.book.title, 'Brave New World')
        self.assertEqual(review.member.first_name, 'Bob')

class TransactionModelTests(TestCase):
    def test_create_transaction(self):
        #create members
        sender = Member.objects.create(
            username='jdoe',
            first_name='Jane',
            last_name='Doe',
            email='jdoe@example.com',
            password='password123'
        )

        receiver = Member.objects.create(
            username='mtwain',
            first_name='Mark',
            last_name='Twain',
            email='mtwain@example.com',
            password='password123'
        )

        #create book
        book = Book.objects.create(
            isbn='2222222222',
            title='To Kill a Mockingbird',
            author='Harper Lee',
            genre='Fiction',
            description='Classic novel on justice and race',
            pub_date='1960-07-11',
            language='English',
            weight=5.0
        )

        #create listing
        listing = BookListing.objects.create(
            book=book,
            member_owner=sender,
            condition='Fair',
            price=15.00
        )

        #create shipment
        shipment = Shipment.objects.create(
            shipment_date='2025-05-02',
            shipment_cost=25.00,
            weight=6.0
        )

        #create transaction
        transaction = Transaction.objects.create(
            transaction_type='Sale',
            transaction_date='2025-05-01',
            shipment=shipment,
            book_listing=listing,
            from_member=sender,
            to_member=receiver,
            cost=38.00,
            swap=None
        )

        self.assertEqual(transaction.transaction_type, 'Sale')
        self.assertEqual(transaction.book_listing.book.title, 'To Kill a Mockingbird')
        self.assertEqual(transaction.from_member.email, 'jdoe@example.com')
        self.assertEqual(transaction.to_member.email, 'mtwain@example.com')
        self.assertEqual(transaction.shipment.shipment_cost, 25.00)










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