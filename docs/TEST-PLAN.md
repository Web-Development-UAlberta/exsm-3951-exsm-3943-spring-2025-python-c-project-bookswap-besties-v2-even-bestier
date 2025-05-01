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
- **Database**: Django ORM
- **Testing Framework**: Django Test Framework, pytest for unit tests
- **CI/CD**: GitHub Actions for continuous integration

---

## 5. Test Case Scenarios

### 5.1 Back End - Database

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| Add Book to Database | Add book with valid data | Book saved to DB | ISBN duplicate, missing data, invalid condition, negative price/weight |
| Register New User | Register with valid inputs | User created with hashed password | Duplicate email, invalid email format, weak password |
| Wishlist Entry | Create wishlist entry | Wishlist record created | Book already in wishlist, book or member missing |
| Reviews | Add review to book | Review saved with valid rating | Rating <1 or >5, empty review, book/member not found |
| Sales Record | Link buyer, seller, and book | Sale saved | Book already sold, invalid user references |


### 5.2 Back End – Functions & Validations

| **Test Case** | **Description** | **Expected Result** | **Error Conditions** |
|---------------|-----------------|---------------------|----------------------|
| Register User | Valid registration data | Success | Email exists, weak password |
| Login User | Valid login | Session created | Invalid credentials |
| Add Book | Valid book info | Book saved | Missing fields, invalid condition, future pub_date |
| Add Book (Edge) | Max-length title, zero price | Book accepted if valid | Title too long, price < 0 |
| Submit Review | Valid rating and comment | Review saved | Rating out of bounds, missing fields |
| Submit Review (Edge) | Empty review or long comment | Error shown or truncated | Validation error |
| Wishlist Entry | Add new wishlist item | Entry created | Book already in wishlist |
| Search Books | Query title, author | Matched books shown | No results found |
| Search (Edge) | Special chars, case-insensitive | Handled gracefully | No results or XSS prevented |


### 5.3 Front End – Forms & UI Validation

| **Form** | **Test Case** | **Expected Result** | **Error Conditions** |
|----------|---------------|---------------------|----------------------|
| Registration | Valid email/password | User registered | Duplicate or invalid email, blank password |
| Registration | Empty/invalid fields | Show field-level errors | All required fields marked |
| Add Book | Submit full book info | Book appears in library | Negative price/weight, invalid date |
| Add Book | Exceed max field lengths | Error or truncation | Title/author too long |
| Review Form | Rating 1–5 with comment | Review posted | Rating out of bounds, empty text |
| Wishlist | Add unique book | Added to wishlist | Already exists, show error |
| Wishlist | Remove book | Wishlist updated | Gracefully handle invalid ID |
| Search | Case-insensitive / partial query | Results returned | No matches handled without error |


### 5.4 Edge Case & Boundary Matrix

| **Component** | **Edge Case** | **Expected Behavior** |
|---------------|---------------|------------------------|
| Registration | Duplicate or invalid email | "Email already in use" error |
| Password | Too short or blank | Validation error |
| Book Listing | Title = 100 chars | Saved successfully |
| Book Listing | Price = 0 or negative | Rejected or flagged |
| Book Listing | Future publication date | Rejected |
| Book Listing | Invalid condition | Not allowed (use enum choices) |
| Reviews | Rating = 0 or 6 | Validation error |
| Reviews | Extremely long review | Truncated or limited |
| Wishlist | Add duplicate book | Show "Already in wishlist" |
| Search | Special characters | Does not crash, returns 0 or escape output |
| Search | Case-insensitive input | Should match title/author |

---

## 6. Test Execution

- **Manual Testing**: UI flows and validation cases
- **Unit Testing**: Automated tests on models and views
- **Front-End Testing**: Form and input validation checks
- **Edge Case Testing**: Verify uncommon and invalid user actions

---

## 7. Expected Outcomes

- All functional tests pass with correct results
- Forms enforce all constraints with useful feedback
- Edge cases handled safely and gracefully
- Clear user feedback on all invalid inputs

## 8. Test Reporting

- **Pass**: Feature performs as expected
- **Fail**: Unhandled error, broken logic, incorrect result