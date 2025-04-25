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
| **Test: Add Book to Database** | Test the addition of a new book to the database | Book is added with correct details | Missing details, duplicate ISBN |
| **Test: Register New User** | Test user registration process | User is created with hashed password | Duplicate email, weak password |

### 5.2 Back End - Functions

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| **Test: Register User** | Register a new user | User is successfully registered | Invalid email format, password too short |
| **Test: Search Books** | Search for books by title | Returns list of books matching the query | No books found for query |

### 5.3 Front End

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| **Test: Login Page** | User submits login form | Redirects to homepage or shows error message | Incorrect credentials |
| **Test: Book Listing Form** | User adds a book to their library | Book appears in library view | Missing fields, incorrect book data |

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