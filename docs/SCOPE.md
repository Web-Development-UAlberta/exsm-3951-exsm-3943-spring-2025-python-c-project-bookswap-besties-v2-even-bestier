# Project Scope Document

## Project Title
**Book Exchange Platform**

## Project Overview

This app is designed for book lovers who want to exchange, sell, or buy books through an intuitive and intelligent system. Users can list books they own and want, and the system will match them for swaps or sales using book metadata and value-aware logic. The platform supports advanced search, user profiles with reviews, condition tracking, and shipping calculations. It is a community-focused project aiming to modernize how people share books.

---

## Project Goals

- Facilitate fair and flexible book exchanges, sales, and purchases.
- Provide intelligent swap suggestions that account for book value.
- Enable users to manage their personal libraries and wishlists.
- Ensure a seamless user experience with search, filtering, and notification tools.
- Simulate core e-commerce features.

---

## Key Features

### 📚 Book Listings
- Users can list books they **own**, **want**, or **have read**.
- Listings include:
  - Title, author, ISBN
  - Transaction type: Buy, Sell, or Swap
  - Book condition: standardized rating (New, Like New, Used, Poor)
  - Cash value or suggested trade value

### 🤝 Matching & Swapping Logic
- System suggests swap matches based on:
  - Wishlist and owned books
  - Value equivalence (e.g., 3x$10 = 1x$30)
  - Up to **3 rounds of counter-offers** allowed per negotiation

### 🔍 Search & Filtering
- Search by:
  - Title, author, genre, publishing date range, price range
- Filter by:
  - Condition, transaction type, user rating, location (optional)

### 👤 User Accounts & Profiles
- Register/login/logout
- Personal library and wishlist
- Review and rating history
- Saved payment/shipping preferences

### ⭐ Ratings & Reviews
- Users can rate/review books they’ve acquired
- Reviews visible in book detail and user profiles

### 🚚 Shipping & Delivery
- Shipping cost calculated based on:
  - Book weight and dimensions
  - User and recipient zip codes (mocked data)
- Simulated label processing (no real integration)

### 🔔 Wishlist & Notifications
- Users get alerts when a desired book becomes available
- Notifications for swap offers, counter-offers, and order status

---

## Deliverables & Timeline

### 📅 Week 01
- [ ] Team Norms Document: `./docs/TEAM-NORMS.md`
- [ ] Scope Document Draft: `./docs/SCOPE.md`
- [ ] Design Document Draft: `./docs/DESIGN.md`
- [ ] Configure GitHub Repository
  - Protect `main` from direct commits
  - Require 2 approvals for PRs

---

### 📅 Week 02
- [ ] Draft ERD v1: `./docs/ERD.drawio`
- [ ] Final Design Document
- [ ] Final Scope Document: `./docs/SCOPE.md`
- [ ] Add in-scope features to GitHub Issues
- [ ] Draft Wireframes: `./docs/wireframes/*.drawio` or `.fig`
  - Include `id`/`class` names for testable UI elements
- [ ] Draft ERD v2
- [ ] Draft Test Plan: `./docs/TEST-PLAN.md`

---

### 📅 Week 03
- [ ] Final ERD: `./docs/ERD.drawio` (Due Sunday)
- [ ] Final Wireframes
- [ ] Final Test Plan
- [ ] Implement Object-Relational Model
- [ ] Begin Back-End Unit Tests
- [ ] Enable CI via GitHub Actions (all branches)

---

### 📅 Week 04
- [ ] ORM Implementation Continued
- [ ] README Setup/Startup: `./docs/README.md`
- [ ] Begin Drafting Business Logic (Swaps, Matching, etc.)
- [ ] Implement Front-End Tests
- [ ] CI auto-build and testing on all branches

---

### 📅 Week 05
- [ ] Finalize Business Logic Implementation
- [ ] Add Project Usage Section to README
- [ ] Publish "Release Candidate" version

---

### 📅 Week 06
- [ ] Final Project Presentation
- [ ] Final Revisions Post-Presentation
- [ ] ✅ All Tests Must Pass

---

## Business Rules

- Users must be able to list books and specify transaction type.
- System matches based on wishlist and available inventory.
- Swap matching must support unequal-value combinations.
- Ratings and condition affect matching and display.
- Counter-offer system is limited to 3 exchanges per negotiation.
- Shipping is calculated using mocked location and weight data.
- All data is stored in a relational DB and modeled with an ERD.

---

## Risks & Constraints

- Swap logic complexity may require iterative development.
- Shipping cost calculation depends on mocked/est. data.
- Counter-offer tracking and negotiation logic needs testing.
- No real payment or shipping service integration (mocked only).

---

## Success Criteria

- Users can register and manage book listings and profiles.
- Swaps, purchases, and sales flow through clearly.
- Matching system suggests value-balanced trades.
- Ratings, reviews, and book conditions are fully integrated.
- All tests pass and CI/CD processes run cleanly.
- System is demo-ready and stable by final presentation.

---