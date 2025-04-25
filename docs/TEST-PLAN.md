# Test Plan for Book Exchange Platform

## 1. Overview
This test plan is designed to ensure that the core features of the **Book Exchange Platform** work as expected. It includes tests for user registration, login, book listing, wishlist functionality, and browsing, as well as essential backend validations.

## 2. Test Scope

### 2.1 Features to be Tested
- **User Registration & Login**:
  - Register a new user.
  - Login with valid and invalid credentials.

- **Book Listing**:
  - Add a book to the library.
  - Validate book details (title, author, condition, etc.).
  
- **Wishlist Management**:
  - Add and remove books from the wishlist.
  
- **Book Browsing and Searching**:
  - Filter books by title, author, price, and condition.
  
- **Reviews**:
  - Add, edit, and delete reviews for books.

### 2.2 Features Not to be Tested
- **Swap Logic**: This will be tested in Phase 2.
- **Shipping/Payment Integration**: These are mocked in Phase 1.

---

## 3. Test Strategy

### 3.1 Test Types
- **Manual Tests**: For UI and UX verification.
- **Unit Tests**: For backend validation and core functionality.
- **Front-End Tests**: To ensure correct behavior of the front end.

---

## 4. Test Environment

- **Backend**: Django
- **Frontend**: Django Template
- **Database**: Django
- **Testing Framework**: Django Test Framework, pytest for unit tests
- **CI/CD**: GitHub Actions for continuous integration

---

## 5. Test Case Scenarios

### 5.1 Back End - Database

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| **Test: Add Book to Database** | Test the addition of a new book to the database | Book is added with valid member and genre reference | Missing details, duplicate ISBN, genre/member not found, duplicate listing |
| **Test: Register New User** | Test user registration process | User is created with hashed password and unique email | Duplicate email, weak password, invalid email format |
| **Test: Wishlist Entry** | Test the creation of a wishlist entry into the database | Wishlist entry created linking book to user | Book or member does not exist, book already in wishlist |
| **Test: Sales** | Test the sales record | Sales record created linking buyer, seller and book | Book or user does not exist, book already sold |
| **Test: Reviews** | Test creation of a review | Review saved with rating and comment for a book | Book or user not found, rating out of range (>5 or <1)

### 5.2 Back End - Functions

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| **Test: Register User** | Register a new user | User is successfully registered with hashed password | Missing or invalid email, password too short/weak, email already exists |
| **Test: Login User** | User Login | Returns session on success | Email not found, incorrect password |
| **Test: Add Book** | Add a book | Book saved with correct references | Missing fields, member doesn't exist |
| **Test: Wishlist Entry** | Add a book onto wishlist | Book added to user's wishlist | Book already in wishlist, invalid IDs |
| **Test: Search Books** | Search for books by title | Returns list of books matching the query | No books found for query |
| **Test: Submit Review** | Save a review on a book | Review saved | Rating invalid, book not found |

### 5.3 Front End

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| **Test: Login Page** | User submits login form | Redirects to homepage or shows error message | Incorrect credentials |
| **Test: Registration Page** | User registers on platform | Displays form, shows success or redirects | Shows errors from 400, 5XX is generic "Try again later." |
| **Test: Book Listing Form** | User adds a book to their library | Book appears in library view | Missing fields, incorrect book data |
| **Test: Wishlist** | View user's wishlist | Shows books from user's wishlist, links to matches | No wishlist with no message for user |
| **Test: Search Books** | Search for books | Filters/search update query | No matches with no message for user |

---

## 6. Test Execution

- **Manual Testing**: Test all UI flows based on the above scenarios.
- **Unit Testing**: Run automated tests for models and views using Django's test framework.

---

## 7. Expected Outcomes

- All tests should pass without errors or unexpected behavior.
- The system should handle edge cases like missing input and invalid data gracefully.
- User flows should be smooth, with clear error messages for invalid actions.

## 8. Test Reporting

- **Pass**: All expected results met.
- **Fail**: Unexpected error or behavior not matching expected results.