# University of Alberta - EXSM 3951 - Python Project 
### Project Name: BookSwap Besties V2 Even Bestier

**Project Authors:** 
 + Nancy Randell, 
 + Justin Bertok, 
 + Diana Cuccarolo
<br>
<br>

## Django Setup/Startup when joining the group as a developer:

1. Clone the repo into your github Repo

    ```bash
    git clone https://github.com/Web-Development-UAlberta/exsm-3951-exsm-3943-spring-2025-python-c-project-bookswap-besties-v2-even-bestier.git
    cd exsm-3951-exsm-3943-spring-2025-python-c-project-bookswap-besties-v2-even-bestier
    ```
2. Python `3.13` is the version used in this project

3. Create a virtual environment for the python project (recommended)
    ```
    python -m venv venv
    ```
4. Activate the virtual environment
    
    For mac/linux:
    ```
    source venv/bin/activate
    ```
    
    For windows:
    ```
    venv/Scripts/activate
    ```
    After the venv is activated, you should see `(venv)` in the terminal prompt
5. Install project dependencies:
    ```
    pip install -r requirements.txt
    ```

6. For the first time, run all migrations
    ```
    python src/exsm3951_bookswap/manage.py migrate 
    ```
7. Now you are ready to run the server
    ```
    python src/exsm3951_bookswap/manage.py runserver 
    ```
8. Once the server is running you can visit the app at http://127.0.0.1:8000/



## Project Usage

A walk through of the User Flow:

### 1. Register a new account
- On the login page, click to register
- Then fill in the information requireed to register a new account (username, passowrd, etc...)

### 2. Login
- Once you have signed up, on the login page enter your credentials (username, password) to log in

### 3. Profile Page
- To update your profile info, navigate to the Profile Page
- There you need to update the full name, email, shipping address, and book genre preference

### 4. Browse for books that I'm interested in
- On the navbar, click on Browse
- Then search for a book by their isbn / title / author / genre
- A popup will display the result where you can click on edit/save to add the book to the library of the app (if it hasn't been added yet)

### 5. Add a book to your wishlist
- Any book present in the library can be added to your wishlist so that you could be notified when there are book listings of that book
- Wishlisted books are listed on the home page under "My Wishlist"

### 6. Make a listing for a book you own
- Once a book is present in the library (after being added from a search on the browse page), you can create a book listing for a copy you own of that book
- On the Books listings page, you can click to create a new book listing
- When creating a book listing you can set the condition and price you want to sell the book for.

### 7. Request book listing from seller to buy
- On the Books Listings page,  you can search for a book to see if there is a listing(s)
- If you find a listing you want to buy, you can click on the "Request Buy" button which will notify the seller to approve or reject the offer.
- If approved, the seller will finalize the details of the sale transaction, and you will be notified that you bought the book with the shipping details
- If the seller rejected, you will be notified of it

### 6. Request book listing to swap
- On the Books Listing page, you can search for a book to see if there is a listing(s)
- If you find a listing you are interested in and you want to offer to swap your book listing(s) with theirs, then you can click the "Offer Swap" button
- You will then be presented with a form to fill with the swap details (Which book listing you are offering)
- Once you confirm your swap offer, the seller be notified of it
- If approved, the seller will finalize the details of the swap transaction, and you will be notified that your swap has been accepted with the shipping details
- If the seller rejected the swap, you will be notified of  it





 


