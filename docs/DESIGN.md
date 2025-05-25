# Software Design Document: Book Exchange System

## 1. Introduction
### 1.1 Purpose
This document outlines the architecture and detailed design for the Book Exchange Platform, a web-based application designed for book lovers to exchange, buy, or sell books. The platform leverages intelligent matching, value-aware swap logic, and community-driven features to create a seamless and engaging user experience.
### 1.2 Scope
The Book Exchange Platform will enable users to:
- List books they own, want, or have read.
- Propose trades, make purchases, or sell books directly.
- Match with other users based on book preferences and value.
- Rate and review books and transaction experiences.
- Search and filter the catalog by genre, author, date, price, and more.
- Track shipping and delivery costs (mocked).
- Receive notifications for wishlist matches and counter-offers.
### 1.3 Definitions
- **Book Exchange Platform**: The web-based application described in this document.
- **User**: Any registered member of the platform with access to its features.
- **Listing**: A book added to the platform with information on ownership and transaction preferences.
- **Swap**: A trade proposal between users, potentially involving multiple books.
- **Counter-offer**: A negotiation response to a swap proposal, with up to 3 permutations allowed.
- **Wishlist**: A list of books a user is actively seeking.
- **Condition Rating**: A standardized metric describing a book’s physical state (e.g., New, Like New, Used, Poor).

## 2. System Architecture
### 2.1 High-Level Architecture
TMS follows a three-tier architecture:
- Presentation Layer (Frontend)
- Application Layer (Backend)
- Data Layer (Database)
### 2.2 Technology Stack
- Frontend: Django
- Backend: Django
- Database: Django
- Authentication: Django
- Deployment: Django

## 3. Detailed Design
### 3.1 ERD 


![ERD Diagram](../src/exsm3951_bookswap/static/images/ERD%20-%20Book%20Swap-revision.4.drawio%20%284%29.svg)



### 3.2 Database Schema

**Member** {\
  "_id": ObjectId,\
  "first_name": String,\
  "last_name": String,\
  "address": String\
  "email": String,\
  "password_hashed": String (hashed),\
  "genre_preference": String,\
}

**Book** {\
  "_id": ObjectId,\
  "title": String,\
  "isbn": String,\
  "author": String,\
  "genre": String,\
  "description": String,\
  "pub_date": DATE,\
  "language": String,\
  "weight": DECIMAL,\
}

**LibraryItem** {\
  "_id": ObjectId,\
  "book_id": ObjectId (ref: Book),\
  "member": ObjectId (ref: Member),\
}

**BookListing** {\
  "book_id": ObjectId (ref: Book),\
  "member_owner": ObjectId (ref: Member),\
  "condition": ENUM(NEW, GOOD, FAIR, POOR),\
  "price": DECIMAL,\
}

**WishList** {\
  "_id": ObjectId,\
  "member": ObjectId (ref: Member),\
  "book": ObjectId (ref: Book),\
}

**Transaction** {\
  "_id": ObjectId",\
  "transaction_type": ENUM(Sale, Swap),\
  "transaction_type": ENUM(Pending, Accepted, Rejected),\
  "transaction_date": DATE,\
  "initiator": ObjectId (ref: Member),\
  "receiver": ObjectId (ref: Member),\
  "initiator": ObjectId (ref: Member),\
}

**TransactoinDetail** {\
  "transaction": (ref: Transaction),\
  "book_listing": ObjectId (ref: BookListing),\
  "from": ObjectId (ref: Member),\
  "to": ObjectId (ref: Member),\
  "shipment": ObjectId (ref: User),\
  "cost": DECIMAL,\
}

**Shipment** {\
  "_id": ObjectId,\
  "shipment_date": Date,\
  "shipement_cost": DECIMAL,\
  "weight": DECIMAL,\
}

**Reviews** {\
  "_id": ObjectId,\
  "member": ObjectId (ref: Member),\
  "book": ObjectId (ref: Book),\
  "rating": Integer,\
  "comment": String,\
}

**Notification** {\
  "_id": ObjectId,\
  "member": ObjectId (ref: Member),\
  "title": String,\
  "is_read": Boolean,\
  "timestamp": Date,\
}


## 4. User Interface Design
### 4.1 Wireframes
#### Key screens include:

- Login/Home
- Browse Books
- My Library, Wishlist, Matches
- Messages and Notifications
- Profile and Shipping Center
- Help and FAQ's

### 4.2 Navigation Structure

#### Home:
- Login / Register
- Featured Books (For Sale / Swap)
- Quick Search
- How It Works

#### Browse Books:
- Search: title, author, genre, ISBN
- Filters:
  - Condition
  - Transaction Type
  - Price Range
  - User Rating
  - Location
- Sort Options
  - Newest
  - Price
  - Condition

#### My Library & Matches & Wishlist:

- Add Book to Library
- Your Books
  - Toggle Available / Unavailable
- Manage Listings
- Suggested Matches
- Pending Reviews (linked to your books)
- Wishlist
  - Wishlist Alerts

#### Messages & Notifications:

- Incoming Swap Offers
- Counter-Offers
- Wishlist Notifications
- Shipping Updates

#### Profile & Shipping Center:

- Edit Account
- Addresses & Payment Info
- View Personal Reviews
- Shipment Tracking (Mocked)
- Generate Shipping Label (Mocked)
- Shipping Cost Estimator (Mocked)

#### Help Center:

- Blog / Guides
- FAQ
- Contact Support

#### Logout:

- Profile Dropdown or Mobile Menu

## 5. Security Considerations
### 5.1 Authentication and Authorization
-	User authentication using Sessions Management (Django authentication)
-	Password hashing (Django automatically hashes passwords)
### 5.2 Data Protection
- HTTPS for all communications
- Input validation and sanitization
- Protection against common vulnerabilities (XSS, CSRF, SQL Injection)

## 6. Testing Strategy

**1. Major Issues**
- Load main views (Home, Browse, Library, Profile)
- Test login/logout
- Add a book
- Open swap flow

 ~15 min per development session

**2. Core User Flows**
- Register -> Add Book -> Mark Available
- Search -> Filter -> View Book -> Request Swap
- Receive -> Accept/Decline Offer
- Wishlist -> Trigger Alert
- View user profile -> See reviews

2 hours

**3. Component Spot Checks**
- Form validation
- Button states (enabled/disabled/loading)
- Notifications (trigger + clear)
- Mobile responsiveness

1 hour

**4. Edge Cases**
- Submit empty/invalid forms
- Use long strings or broken inputs
- Access features while logged out
- Duplicate listings
- Invalid URLs

1 hour

**5. Final Polish**
- Fix typos
- Confirm 404/fallback pages
- Responsive layout checks
- User-friendly alerts

1 hour

**(Optional) Automated Tests**
- Login flow
- Search + filter
- Swap request lifecycle

2–3 hours (optional)


## 7. Deployment Plan
### 7.1 Development Environment
- Local development using Django.
- Version control and branching via Git + GitHub.
### 7.2 Staging Environment
- Localhost or test server.
- CI/CD pipeline configured with GitHub Actions.
- Automated testing and linting before merges.
### 7.3 Production Environment
- Target: AWS ECS with auto-scaling and load balancing.
- Live deployment status: **TBD**.

## 8. High Level Timeline and Milestones
**Please see SCOPE.md for further details.**
| Phase | Description                                      | Duration | Target Completion |
|-------|--------------------------------------------------|----------|-------------------|
| 1     | Initial Setup & Project Planning                 | 1 week   | April 21, 2025    |
| 2     | Design Finalization & Early Planning             | 2 weeks  | April 23, 2025    |
| 3     | Finalize Planning Docs & Begin Implementation    | 3 weeks  | April 30, 2025    |
| 4     | Build Core Application Logic                     | 3 weeks  | May 7, 2025       |
| 5     | Finalize Application Logic & Prepare for Release | 2 weeks  | May 14, 2025      |
| 6     | Final Presentation & Project Completion          | 2 weeks  | May 21, 2025      |

## 9. Appendix
### 9.1 References
- [Django Documentation](https://docs.djangoproject.com/en/5.2/)