# 🎬 MovieMate API (IMDb Clone)

A backend REST API built with **Django REST Framework**, inspired by IMDb.
It allows admins to manage movies & streaming platforms, users to review movies (1 review per user per movie), and guests to browse content.

Tested thoroughly with **Postman** for API validation.

---

## 🚀 Features

- **Admin**
  - Add streaming platforms
  - Add movies to watchlist
- **Authenticated Users**
  - Add one review per movie
  - Update/delete their reviews
- **Guests**
  - Browse movies and reviews (read-only)
- **Extra**
  - Pagination & searching in movie list
  - Token-based authentication
  - Automated tests using Django test framework
  - Database seeding script (creates 50 users, 120 movies, 5000+ reviews)

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 4+
- Django REST Framework
- SQLite (default database)
- Postman (API testing)

---

## ⚡ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/moviemate.git
   cd moviemate
