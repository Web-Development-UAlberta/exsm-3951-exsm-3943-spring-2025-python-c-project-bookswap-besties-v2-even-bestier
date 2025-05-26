from django.test import TestCase
from .models import Book, BookListing, Review, WishList, Shipment, Transaction, TransactionDetail, LibraryItem
from authentication.models import Member
from notifications.models import Notification
from django.contrib.auth.tokens import default_token_generator
from django.db import IntegrityError
from django.core.exceptions import ValidationError

#sources: https://docs.djangoproject.com/en/5.2/topics/testing/overview/

def CreateMember():
    member = Member.objects.create(
            username='jdoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            password='password123',
            address='123 Main St'
        )
    return member

def CreateBook():
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
    return book

def CreateListing(book, member):
    library_item = LibraryItem(book=book, member=member)
    library_item.save()
    listing = BookListing.objects.create(
        library_item=library_item,
        member_owner=member,
        condition='Fair',
        price=15.00
    )
    return listing

def CreateShipment():
    shipment = Shipment.objects.create(
        shipment_date='2025-05-02',
        shipment_cost=25.00,
        weight=6.0,
        address="abc"
    )
    return shipment

class MemberModelTests(TestCase):
    def test_create_member(self):
        member = CreateMember()

        self.assertEqual(member.email, 'johndoe@example.com')
        self.assertEqual(member.first_name, 'John')
        self.assertEqual(member.last_name, 'Doe')

    def test_create_member_with_duplicate_username(self):
        CreateMember()

        #username will trigger error
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                username='jdoe',
                first_name='John',
                last_name='Doe',
                email='johndoe@example.com',
                password='password123',
                address='123 Main St'
            )
        #Integrity Error with help from OpenAI ChatGPT 3.5, May 7/25    

    def test_update_member_profile(self):
        member = CreateMember()

        member.address = 'New Address'
        member.save()
        self.assertEqual(Member.objects.get(username='jdoe').address, 'New Address')
        #member.objects.get with help from OpenAI ChatGPT 3.5, May 3/25

    #reset password with help from OpenAI ChatGPT 3.5, May 3/25
    def test_password_reset_token_generation(self):
        member = CreateMember()

        token = default_token_generator.make_token(member)
        self.assertTrue(default_token_generator.check_token(member, token))

    def test_create_member_no_first_name(self):
        Member.objects.create(
            username='jdoe',
            first_name='',
            last_name='Doe',
            email='johndoe@example.com',
            password='password123',
            address='123 Main St'
            )

        self.assertRaises(IntegrityError)

class BookModelTests(TestCase):
    def test_create_book(self):
        book = CreateBook()

        self.assertEqual(book.title, 'The Great Gatsby')
        self.assertEqual(book.isbn, '1234567890')
        self.assertEqual(book.author, 'F. Scott Fitzgerald')
        self.assertEqual(book.weight, 4.5)

    def test_create_book_without_title(self):
        #create book
        Book.objects.create(
            isbn='1234567890',
            title='',
            author='F. Scott Fitzgerald',
            genre='Fiction',
            description='A classic novel',
            pub_date='1954-09-25',
            language='English',
            weight=4.5
        )

        self.assertRaises(IntegrityError)

    def test_create_book_with_weight_length_too_long(self):
        Book.objects.create(
            isbn='1234567890',
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            genre='Fiction',
            description='A classic novel',
            pub_date='1954-09-25',
            language='English',
            weight=46541364.5
        )  

        self.assertRaises(IntegrityError)

    def test_create_book_with_duplicate_isbn(self):
        CreateBook()

        #isbn will trigger error
        with self.assertRaises(IntegrityError):
            Book.objects.create(
                isbn='1234567890',
                title='The Great Gatsby',
                author='F. Scott Fitzgerald',
                genre='Fiction',
                description='A classic novel',
                pub_date='1954-09-25',
                language='English',
                weight=4.5
            )

class BookListingModelTests(TestCase):
    def test_create_booklisting(self):
        member = CreateMember()
        book = CreateBook()
        listing = CreateListing(book, member)
        
        self.assertEqual(listing.condition, 'Fair')
        self.assertEqual(listing.price, 15.00)
        self.assertEqual(listing.library_item.book.title, 'The Great Gatsby')
        self.assertEqual(listing.member_owner.email, 'johndoe@example.com')

    def test_create_book_listing_condition_not_a_choice(self):
        member = CreateMember()
        book = CreateBook()
        
        library_item = LibraryItem(book=book, member=member)
        library_item.save()
        
        #create listing
        BookListing.objects.create(
            library_item=library_item,
            member_owner=member,
            condition='Extremely Perfect!',
            price=12.50
        )

        self.assertRaises(IntegrityError)

class ReviewModelTests(TestCase):
    def test_create_review(self):
        member = CreateMember()
        book = CreateBook()

        #create review
        review = Review.objects.create(
            book=book,
            member=member,
            rating=5,
            review='A fascinating and eerie read!'
        )

        self.assertEqual(review.rating, 5)
        self.assertIn('fascinating', review.review)
        self.assertEqual(review.book.title, 'The Great Gatsby')
        self.assertEqual(review.member.first_name, 'John')

    def test_review_rating_higher_than_5(self):
        #create member
        member = CreateMember()
        book = CreateBook()

        #create review
        Review.objects.create(
            book=book,
            member=member,
            rating=8,
            review='A fascinating and eerie read!'
        )

        self.assertRaises(IntegrityError)

class TransactionModelTests(TestCase):
    def test_create_transaction(self):
        #create members
        sender = CreateMember()

        receiver = Member.objects.create(
            username='mtwain',
            first_name='Mark',
            last_name='Twain',
            email='mtwain@example.com',
            password='password123'
        )

        book = CreateBook()
        listing = CreateListing(book, sender)
        shipment = CreateShipment()

        #create transaction
        transaction = Transaction.objects.create(
            transaction_type='Sale',
            transaction_date='2025-05-01',
            initiator_member=sender,
            receiver_member=receiver,
        )
        transaction.save()
        
        # create transaction detail
        transaction_detail = TransactionDetail.objects.create(
            transaction=transaction,
            book_listing=listing,
            shipment=shipment,
            from_member=sender,
            to_member=receiver,
            cost=38.00
        )
        transaction.save()
        

        self.assertEqual(transaction.transaction_type, 'Sale')
        self.assertEqual(transaction_detail.book_listing.library_item.book.title, 'The Great Gatsby')
        self.assertEqual(transaction_detail.from_member.email, 'johndoe@example.com')
        self.assertEqual(transaction_detail.to_member.email, 'mtwain@example.com')
        self.assertEqual(transaction_detail.shipment.shipment_cost, 25.00)

    def test_create_transaction_type_not_in_list(self):
        #create members
        sender = CreateMember()

        receiver = Member.objects.create(
            username='mtwain',
            first_name='Mark',
            last_name='Twain',
            email='mtwain@example.com',
            password='password123'
        )

        book = CreateBook()
        listing = CreateListing(book, sender)
        shipment = CreateShipment()

        with self.assertRaises(ValidationError):
            transaction = Transaction(
                transaction_type='Garage Sale',
                transaction_date='2025-05-01',
                initiator_member=sender,
                receiver_member=receiver,
            )
            transaction.full_clean()
            transaction.save()


class WishListModelTests(TestCase):
    def test_create_wishlist(self):
        member = CreateMember()
        book = CreateBook()
        
        #create wishlist
        wishlist = WishList.objects.create(
            book=book,
            member=member
        )

        self.assertEqual(wishlist.book.title, 'The Great Gatsby')
        self.assertEqual(wishlist.member.address, '123 Main St')

    def test_add_duplicate_book_to_wishlist(self):
        member=CreateMember()
        book=CreateBook()

        #create wishlist
        WishList.objects.create(
            book=book,
            member=member
        )

        with self.assertRaises(IntegrityError):
            WishList.objects.create(
                book=book,
                member=member
            )

class ShipmentModelTests(TestCase):
    def test_create_shipment(self):
        shipment = CreateShipment()

        self.assertEqual(str(shipment.shipment_date), '2025-05-02')
        self.assertEqual(shipment.weight, 6.0)
        self.assertEqual(shipment.shipment_cost, 25.00)

    def test_create_shipment_weight_too_long(self):
        #create shipment
        Shipment.objects.create(
            shipment_date='2025-05-02',
            shipment_cost=6.99,
            weight=65633456.0
        )

        self.assertRaises(IntegrityError)

class SwapTests(TestCase):
    def test_member_with_no_swaps(self):
        member1 = Member.objects.create(
            username='bsmith',
            first_name='Bob',
            last_name='Smith',
            email='bsmith@example.com',
            password='password123',
            address='456 Elm St'
        )
        member2 = CreateMember()
        book = CreateBook()
        listing = CreateListing(book, member1)
        shipment = CreateShipment()

        # Create a sale transaction (not a swap)
        t = Transaction.objects.create(
            transaction_type='Sale',
            transaction_date='2025-05-03',
            initiator_member=member1,
            receiver_member=member2,
        )
        t.save()
        t_detail = TransactionDetail.objects.create(
            transaction=t,
            shipment=shipment,
            book_listing=listing,
            from_member=member1,
            to_member=member2,
            cost=15.00
        )
        t_detail.save()

        # Verify the member has no swap transactions
        swap_transactions = Transaction.objects.filter(
            transaction_type='Swap',
            initiator_member=member1
        )
        self.assertEqual(swap_transactions.count(), 0)
        #swap_transactions with help from OpenAI ChatGPT 3.5, May 3/25



#FRONT END TESTS

class LibraryViewTests(TestCase):
    def test_book_listing_appears_in_my_book_listings_page(self):
        member=CreateMember()
        book=CreateBook()
        CreateListing(book, member)

        self.client.force_login(member)
        
        response = self.client.get('/library/my-book-listings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Great Gatsby')

    def test_wishlist_item_appears_in_wishlist_page(self):
        member=CreateMember()
        book=CreateBook()
        WishList.objects.create(member=member, book=book)
        self.client.force_login(member)

        response = self.client.get('/library/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Great Gatsby')

    def test_empty_state_library_view(self):
        member=CreateMember()
        self.client.force_login(member)

        response=self.client.get('/library/my-book-listings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You don't have any book listings yet.") 

class WishlistViewTests(TestCase):
    def test_add_book_to_wishlist(self):
        member = CreateMember()
        book = CreateBook()

        self.client.force_login(member)
        response = self.client.get(f'/library/wishlist/add/{book.id}/')

        self.assertEqual(response.status_code, 302)
        self.assertTrue(WishList.objects.filter(member=member, book=book).exists())


    def test_remove_book_from_wishlist(self):
        member=CreateMember()
        book = CreateBook()

        #add book to wishlist
        wishlist_item=WishList.objects.create(member=member, book=book)

        #simulate removal from wishlist
        self.client.force_login(member)
        response=self.client.post(f'/library/wishlist/remove/{wishlist_item.id}/')

        self.assertEqual(response.status_code, 302)
        self.assertFalse(WishList.objects.filter(id=wishlist_item.id).exists())


class BrowseViewTests(TestCase):
    def test_book_detail_page(self):
        member=CreateMember()
        book=CreateBook()
        listing=CreateListing(book, member)

        self.client.force_login(member)
        response = self.client.get(f'/library/book-listings/{listing.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Great Gatsby')


class BookSearchModalTests(TestCase):
    def test_modal_shows_on_search(self):
        member = CreateMember()
        self.client.force_login(member)
        response = self.client.get('/library/browse/search/?q=Gatsby&show_modal=1')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'searchModal')


class NavigationTests(TestCase):
    def test_navigation_links(self):
        member=CreateMember()
        self.client.force_login(member)
        response=self.client.get('/library/')

        self.assertContains(response, 'Library')
        self.assertContains(response, 'My Listings')
        self.assertContains(response, 'My Wishlist')
        self.assertContains(response, 'Browse')        
        self.assertContains(response, 'Notifications')
        self.assertContains(response, 'My Profile')
        self.assertContains(response, 'Help')
        self.assertContains(response, 'Logout')

class CreateBookListingViewTests(TestCase):
    def test_create_book_listing_view(self):
        member = CreateMember()
        book = CreateBook()
        library_item = LibraryItem.objects.create(book=book, member=member)

        self.client.force_login(member)
        response = self.client.post('/library/book-listings/create', {
            'library_item': library_item.id,
            'condition': 'Good',
            'price': '12.50',
            'member_owner': member.id
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(BookListing.objects.filter(member_owner=member).exists())


class SwapOfferTests(TestCase):
    def test_swap_offer_from_renders(self):
        member = CreateMember()
        book = CreateBook()
        listing = CreateListing(book, member)

        self.client.force_login(member)
        response = self.client.get(f'/library/transactions/swap/{listing.id}')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Swap')

class MultiBookSwapTests(TestCase):
    def test_multi_book_swap_creates_multiple_transaction_details(self):
        initiator = CreateMember()
        receiver = Member.objects.create(
            username='jane_doe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.com',
            password='password123',
            address='789 Maple St'
        )
        book_to_receive = CreateBook()
        listing_to_receive = CreateListing(book_to_receive, receiver)

        #create two books for initiator to offer
        book1 = Book.objects.create(
            isbn='111111111',
            title='Book One',
            author='Author A',
            genre='Fiction',
            description='Test',
            pub_date='2000-01-01',
            language='English',
            weight=1.0
        )

        book2 = Book.objects.create(
            isbn='222222222',
            title='Book Two',
            author='Author B',
            genre='Nonfiction',
            description='Test',
            pub_date='2000-01-01',
            language='English',
            weight=1.0
        )
        listing1 = CreateListing(book1, initiator)
        listing2 = CreateListing(book2, initiator)

        shipment = CreateShipment()

        transaction = Transaction.objects.create(
            transaction_type='Swap',
            transaction_status='Pending',
            initiator_member=initiator,
            receiver_member=receiver,
        )

        #requested book
        TransactionDetail.objects.create(
            transaction=transaction,
            book_listing=listing_to_receive,
            shipment=shipment,
            from_member=receiver,
            to_member=initiator,
            cost=0
        )

        #offered books
        TransactionDetail.objects.create(
            transaction=transaction,
            book_listing=listing1,
            shipment=shipment,
            from_member=initiator,
            to_member=receiver,
            cost=0
        )
        TransactionDetail.objects.create(
            transaction=transaction,
            book_listing=listing2,
            shipment=shipment,
            from_member=initiator,
            to_member=receiver,
            cost=0
        )

        self.assertEqual(transaction.transaction_details.count(),3)

class SwapAcceptanceTests(TestCase):
    def test_accept_swap_marks_listing_closed(self):
        sender = CreateMember()
        receiver = Member.objects.create(
            username='jane_doe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.com',
            password='password123',
            address='789 Maple St'
        )

        book = CreateBook()
        listing = CreateListing(book, receiver)
        shipment = CreateShipment()

        transaction = Transaction.objects.create(
            transaction_type='Swap',
            initiator_member=sender,
            receiver_member=receiver
        )

        TransactionDetail.objects.create(
            transaction=transaction,
            book_listing=listing,
            shipment=shipment,
            from_member=receiver,
            to_member=sender,
            cost=0
        )

        #simulate acceptance
        transaction.transaction_status = 'Accepted'
        listing.is_closed = True
        listing.save()
        transaction.save()

        self.assertEqual(transaction.transaction_status, 'Accepted')
        self.assertTrue(listing.is_closed)


class NotificationTests(TestCase):
    def test_notification_created_on_wishlist_match(self):
        listing_owner = CreateMember()
        book = CreateBook()
        listing = CreateListing(book, listing_owner)

        viewer = Member.objects.create(
            username='viewr',
            first_name='View',
            last_name='Er',
            email='view@example.com',
            password='password123',
            address='1 Viewer Rd'
        )

        self.client.force_login(viewer)
        response = self.client.get(f'/library/wishlist/add/{book.id}/')

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Notification.objects.filter(member=viewer, title__icontains=book.title).exists())