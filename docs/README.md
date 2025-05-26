# 📚 University of Alberta - EXSM 3951
## **Project Name: BookSwap Besties V2 Even Bestier**

**Project Authors:** 
 + Nancy Randell, 
 + Justin Bertok, 
 + Diana Cuccarolo

---

## 📝 Description

**BookSwap** is a community-driven platform built for book lovers to easily swap, sell, or buy books from one another. We believe in the power of sharing stories and knowledge through books.  

Our mission is to create a seamless, fair, and friendly environment where users can connect, exchange, and enjoy books—whether through trade, sale, or purchase.

The platform offers a robust set of features to help users manage their personal library, wishlist, and transaction history. Whether you're looking to track down a rare book or offer your own collection, BookSwap is your go-to space for all things book exchange.

---

## 🚀 Project Setup & Startup

### Prerequisites
- Python 3.13
- Git (to clone the repository)

### Installation Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/Web-Development-UAlberta/exsm-3951-exsm-3943-spring-2025-python-c-project-bookswap-besties-v2-even-bestier.git
    cd exsm-3951-exsm-3943-spring-2025-python-c-project-bookswap-besties-v2-even-bestier
    ```
2. **(Recommended) Create a virtual environment**
    ```bash
    python -m venv venv
    ```
3. **Activate the virtual environment**
    
    - macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

    - Windows:
        ```bash
        venv\Scripts\activate
        ```
    - After the venv is activated, you should see `(venv)` in the terminal prompt

4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run database migrations**
    ```bash
    python src/exsm3951_bookswap/manage.py migrate 
    ```
6. **Start the development server**
    ```bash
    python src/exsm3951_bookswap/manage.py runserver 
    ```
7. Visit the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)



## 👨‍💻 Project Usage – User Flow Walkthrough

### 1. Register a New Account
- On the login page, click "Register".
- Fill in your username, password, and other required information.

### 2. Login
- Enter your credentials to access your account.

### 3. Update Profile
- Go to the Profile Page.
- Add your full name, email, shipping address, and genre preferences.

### 4. Browse for Books
- Click "Browse" in the navbar.
- Search by ISBN, title, author, or genre.
- A popup will display results. Add books to the library if they aren't already listed.

### 5. Wishlist a Book
- Add any book in the library to your wishlist.
- Wishlisted books appear on your homepage under “My Wishlist”.

### 6. List a Book for Sale
- Add a listing for any book in the library.
- Set the condition and price for your book.

### 7. Buy a Book
- Search available listings.
- Click "Request Buy" to notify the seller.
- Seller approves or rejects your request.
- If approved, you'll be notified and receive shipping details.

### 8. Swap a Book
- Search for listings.
- Click "Offer Swap" and choose one of your own listings to offer.
- Seller approves or rejects the offer.
- You'll be notified of the outcome.

---

## ✅ Features

- 📚 Manage personal book listings  
- 🔎 Search by ISBN, title, author, or genre  
- 💖 Wishlist system with notifications  
- 🔄 Book swapping functionality  
- 💸 Secure buy/sell listings  
- 🛠️ User profile management  

---

## 🧪 Running Tests

To run the test suite:

    ```bash
    python src/exsm3951_bookswap/manage.py test
    ```

## Citations & Acknowlegements

help.html: ChatGPT. (2025). JavaScript code for toggle FAQ answers on click. OpenAI. Retrieved from https://chat.openai.com

settings.html: OpenAI. (2025). Mock shipping form with confirmation modal using HTML, Tailwind CSS, and JavaScript. ChatGPT (May 17, 2025) response. https://chat.openai.com/

tests.py: Integrity Error with help from OpenAI ChatGPT 3.5, May 7/25 
tests.py: member.objects.get with help from OpenAI ChatGPT 3.5, May 3/25
tests.py: reset password with help from OpenAI ChatGPT 3.5, May 3/25
tests.py: swap_transactions with help from OpenAI ChatGPT 3.5, May 3/25

browse.html/views.py: OpenAI. (2025). Implementing form-based filtering in Django views and templates using GET parameters. ChatGPT. Retrieved from https://chat.openai.com/

## 📬 Contact
For any questions or support, feel free to contact the authors via the course forum or GitHub issues.


