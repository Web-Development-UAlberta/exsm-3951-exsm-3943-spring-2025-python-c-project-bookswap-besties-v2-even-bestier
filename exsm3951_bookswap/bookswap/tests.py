from django.test import TestCase
from .models import Book, BookListing, Review, WishList, Shipment, Swap, Transaction
from authentication.models import Member

#sources: https://docs.djangoproject.com/en/5.2/topics/testing/overview/

class MemberModelTests(TestCase):
    def test_create_member(self):
        member = Member.objects.create(
            member_name='John Doe',
            email='johndoe@example.com',
            password='password123'
        )
        self.assertEqual(member.email, 'johndoe@example.com')

class BookModelTests(TestCase):
    def text_create_book(self):
        member = Member.objects.create(
            member_name='Jane Doe',
            email='janedoe@example.com',
            password='password123'
        )
        book = Book.objects.create(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            member=member,
            genre='Fiction',
            description='A classic novel',
            pub_date='09/25/1954',
            language='English',
            weight='4.5'
        )
        self.assertEqual(book.title, 'The Great Gatsby')

class BookViewTests(TestCase):
    def test_book_listing_view(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Great Gatsby')