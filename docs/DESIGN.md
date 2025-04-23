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

<img src="../images/Book Swap ERD.jpg" width="1000" height="648">

### 3.2 Database Schema

**Members** {\
  "_id": ObjectId,\
  "member_name": String,\
  "email": String,\
  "password": String (hashed),\
  "address": String\
}

**Books** {\
  "_id": ObjectId,\
  "member": ObjectId (ref: Members),\
  "title": String,\
  "author": String,\
  "genre": ObjectId (ref: Genres),\
  "description": String,\
  "pub_date": DATE,\
  "condition": String,\
  "language": String,\
  "price": DECIMAL,\
  "weight": DECIMAL,\
}

**Wish_Lists** {\
  "_id": ObjectId,\
  "member": ObjectId (ref: Members),\
  "book": ObjectId (ref: Books),\
}

**Genres** {\
   "_id": ObjectId,\
   "genre": String,\
}

**Sales** {\
  "_id": ObjectId,\
  "seller": ObjectId (ref: Members),\
  "buyer": ObjectId (ref: Members),\
  "book": ObjectId (ref: Books),\
  "shipment": ObjectId (ref: Users),\
}

**Shipments** {\
  "_id": ObjectId,\
  "shipment_date": Date,\
  "address": ObjectId (ref: Members),\
  "cost": Decimal,
}

**Swaps** {\
  "_id": ObjectId,\
  "shipment": ObjectId (ref: Members),\
}

**Swap_Details** {\
  "_id": ObjectId,\
  "book": ObjectId (ref: Books),\
  "original_owner": ObjectId (ref: Members),\
  "new_owner": ObjectId (ref: Members),\
  "swap": ObjectId (ref: Swaps),\
}

**Reviews** {\
  "_id": ObjectId,\
  "member": ObjectId (ref: Members),\
  "book": ObjectId (ref: Books),\
  "rating": Integer,\
  "comment": String,\
}


## 4. User Interface Design
### 4.1 Wireframes
#### Key screens include:
- Dashboard
- Project List/Detail View
- Task List/Detail View
- User Profile
- Admin Panel
### 4.2 Navigation Structure

Home
├── Dashboard
├── Projects
│   ├── Project List
│   └── Project Details
├── Tasks
│   ├── My Tasks
│   ├── Team Tasks
│   └── Task Details
├── Reports
└── Settings
    ├── Profile
    ├── Notifications
    └── Team Management (Admin only)

## 5. Security Considerations
### 5.1 Authentication and Authorization

+	User authentication using Sessions Management (Django authentication)
+	Password hashing (Django automatically hashes passwords)

### 5.2 Data Protection

+ HTTPS for all communications
+	Input validation and sanitization.
+	Protection against common vulnerabilities (XSS, CSRF, SQL Injection)

## 6. Testing Strategy
- "[To be filled in later]"

## 7. Deployment Plan
### 7.1 Development Environment
- Django for local development.
### 7.2 Staging Environment
- Local Host with CI/CD pipeline via GitHub Actions.
### 7.3 Production Environment
- AWS ECS with auto-scaling and load balancing. (Live deployment TBD)

## 8. Timeline and Milestones
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