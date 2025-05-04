# Test Plan for Book Exchange Platform

## 1. Overview
This test plan is designed to ensure that the core features of the **Book Exchange Platform** work as expected. It includes tests for user registration, login, book listing, wishlist functionality, and browsing, as well as essential backend validations.

## 2. Test Scope

### 2.1 Features to be Tested
- **User Registration & Login**:
  - Register a new user.
  - Login with valid and invalid credentials.
  - Password reset flow
  - Update user profile (e.g., name, address, genre preference)

- **Book Listing**:
  - Add a book to the library.
  - Validate book details (title, author, condition, etc.).
  
- **Wishlist Management**:
  - Add and remove books from the wishlist.
  
- **Book Browsing and Searching**:
  - Filter books by title, author, price, and condition.
  
- **Reviews**:
  - Add, edit, and delete reviews for books.
  - Rating validation

- **Swaps**
  - Create swap transactions (single or multiple books)
  - Support swap negotiation (offer, counter-offer)
  - Handle disputed swaps or cancellations
  - Record shipment details and handle damage claims

- **Shipment**
  - Record shipment info and validate cost, weight, and date

### 2.2 Features Not to be Tested
- **Real Payment Processing**: Mocked in Phase 1
- **Shipping Label Integration**: Phase 2

---

## 3. Test Strategy

### 3.1 Test Types
- **Manual Tests**: For UI/UX flows and messages
- **Unit Tests**: For models, views, forms
- **Front-End Tests**: Input validation and feedback
- **Edge Case Tests**: Validate system resilience
- **Integration Tests**: Complex workflows like swaps + shipment + transaction

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

| **Test Case**           | **Description**                     | **Expected Result**             | **Error Conditions**                                |
|-------------------------|-------------------------------------|---------------------------------|-----------------------------------------------------|
| Add Book                | Save valid book                     | Book saved to user's library    | Invalid/missing fields                              |
| Add Book (Zero Price)   | Price = 0                           | Book accepted (e.g., donation)  | Negative price rejected                             |
| Register User           | Save valid user                     | User created                    | Duplicate email/username                            |
| Password Reset          | Trigger password reset              | Email sent                      | Invalid email shows error                           |
| Update Profile          | Edit user details                   | Profile updated                 | Missing required fields                             |
| Wishlist Entry          | Add book to wishlist                | Entry saved                     | Duplicate entry blocked                             |
| Review                  | Add review with rating 1–5          | Review saved                    | Invalid rating                                      |
| Sale Transaction        | Record buyer/seller/book            | Transaction saved               | Invalid refs or duplicate                           |
| Swap – Basic            | One-for-one swap                    | Swap saved                      | Missing refs or data                                |
| Swap – Multi-Book       | Multiple-for-one swap               | All books linked correctly      | Book reused in other swap                           |
| Swap – Negotiation      | Create and respond to offers        | Status updated                  | Invalid offer logic                                 |
| Swap – Dispute          | Dispute after swap                  | Flag swap, log dispute          | No resolution handler                               |
| Shipment                | Record shipment                     | Shipment saved                  | Negative cost, invalid date                         |
| Damaged Book Claim      | Report damaged book                 | Damage record linked            | Missing description                                 |


### 5.2 Back End – Functions & Validations

| **Test Case**           | **Description**              | **Expected Result**         | **Error Conditions**                            |
|-------------------------|------------------------------|-----------------------------|--------------------------------------------------|
| Register User           | Valid info                   | Success                     | Duplicate email                                  |
| Login                   | Valid credentials            | Session starts              | Invalid creds show error                         |
| Add Book                | Max-length title, 0 price    | Saved if valid              | Negative values rejected                         |
| Submit Review           | Rating + text                | Review saved                | Rating outside 1–5                               |
| Wishlist                | Add/remove                   | Entry created/removed       | Already exists                                   |
| Search Books            | Title, author, etc.          | Matches shown               | No results gracefully handled                    |
| Swap Initiation         | Offer valid swap             | Swap saved                  | Missing book/member                              |
| Swap Update             | Counter or cancel swap       | Status reflects change      | Invalid state transition                         |
| Swap Dispute            | Initiate dispute             | Logged properly             | Already resolved                                 |
| Damaged Shipment        | Report and attach book       | Status = damaged            | Missing damage info                              |
| Shipment Entry          | Add shipment                 | Validated and saved         | Invalid cost/date                                |



### 5.3 Front End – Forms & UI Validation

| **Form**         | **Test Case**                     | **Expected Result**          | **Error Conditions**                            |
|------------------|-----------------------------------|------------------------------|--------------------------------------------------|
| Registration      | Valid input                      | Account created               | Invalid/duplicate email                          |
| Password Reset    | Enter email                      | Email sent                    | No email: show message                           |
| Profile Edit      | Update name/address              | Info updated                  | Blank required fields                            |
| Add Book          | Fill all fields                  | Book appears in user library  | Validation on blanks/invalids                    |
| Review            | Submit rating + comment          | Saved/reviewed                | Rating invalid                                   |
| Wishlist          | Add/remove book                  | Updated live                  | Already in list                                  |
| Search            | Case-insensitive queries         | Matched shown                 | Empty result = friendly message                  |
| Swap Offer        | Choose book + user               | Offer created                 | Missing selection                                |
| Swap History      | View completed swaps             | List shown or empty message   | No swaps = show empty state                      |
| Shipment          | Add weight/cost/date             | Saved                         | Negative numbers = error                         |



### 5.4 Edge Case & Boundary Matrix

| **Component**        | **Edge Case**                        | **Expected Behavior**                   |
|----------------------|--------------------------------------|------------------------------------------|
| Registration         | Duplicate email                      | “Email in use” shown                     |
| Password             | Too short                            | Error shown                              |
| Book Title           | 100 characters                       | Saved                                    |
| Price                | 0 (donation)                         | Allowed                                  |
| Price                | Negative                             | Rejected                                 |
| Pub Date             | Future date                          | Rejected unless marked “Pre-order”       |
| Condition            | Invalid enum                         | Rejected                                 |
| Review Rating        | 0 or 6                               | Validation error                         |
| Long Review          | >10,000 chars                        | Truncate or block                        |
| Wishlist             | Add same book again                  | Show error                               |
| Search               | Special chars                        | Escaped; no crash                        |
| Swap                 | Same book in two swaps               | Block duplicate use                      |
| Disputed Swap        | Swap flagged by user                 | Alert admin/moderator                    |
| Shipment             | Cost = -1                            | Error message                            |
| Swap History         | User has 0 swaps                     | Show “no history yet”                    |
| Unauthorized Access  | Not logged in                        | Redirect to login                        |


---

## 6. Test Execution

- **Manual Testing**: Run UI interactions across various devices and browsers.
- **Automated Unit Tests**: Use Django TestCase for backend validations and model logic.
- **Integration Tests**: Cover combined workflows such as "book listing → swap → shipment".
- **Edge Case Testing**: Simulate unexpected user behavior, missing fields, invalid data.
- **Continuous Testing**: Use GitHub Actions or other CI pipelines to run tests on push/merge.

---

## 7. Expected Outcomes

- Functional workflows like registration, login, listing, and swaps work end-to-end.
- Validation and error messaging are user-friendly and consistent.
- Edge cases are handled gracefully (e.g., invalid inputs, duplicate entries).
- Data consistency is preserved across books, swaps, and transactions.
- Unauthorized access and invalid operations are blocked.

## 8. Test Reporting

- **Pass**: Feature performs as expected
- **Fail**: Unhandled error, broken logic, incorrect result
- Use GitHub CI or a testing dashboard for automated logging and alerts.