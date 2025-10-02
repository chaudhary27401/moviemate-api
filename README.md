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
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Install dependencies:
     ```bash
  
    pip install -r requirements.txt


5. Apply migrations:
    ```bash
    python manage.py migrate


5. (Optional) Seed the database with users/movies/reviews:
    ```bash
    python manage.py seed_data


6. Run server:
    ```bash
    python manage.py runserver
7. Urls:
     <br/> Note: Use all the urls in Postman API tool as it is totally backend project
     <br/> To register user
     ```bash
        https://moviemate-r98s.onrender.com/accounts/register/  
     ```
     <br/> To login user (to obtain your token)
     ```bash
       https://moviemate-r98s.onrender.com/accounts/login
     ```
     <br/> To logout user (Input your token in postman tool)
     ```bash
       https://moviemate-r98s.onrender.com/accounts/logout/
     ```
     
     
     ```bash
     
     https://moviemate-r98s.onrender.com/movies/list/  #To list all the movies
     https://moviemate-r98s.onrender.com/movies/stream/<int:pk>/review-create/  #To create a review about movie replace int with movie number and first you should be logged in.
     https://moviemate-r98s.onrender.com/movies/stream/<int:pk>/review/  # To watch the reviews, you should be authenticated for this.
     https://moviemate-r98s.onrender.com/movies/stream/review/<int>  #To know about specific review
     https://moviemate-r98s.onrender.com/movies/reviews/?username=Your_Username   # To get the specific username queries
     https://moviemate-r98s.onrender.com/movies/watch-filter?platform=platform_name   #To get the specific platform detail
     https://moviemate-r98s.onrender.com/movies/watch-filter?title=Movie_Title   # To search for title
     ```
     
     
    
   

Screenshots:
  <br/> For Reference Default platforms names are:
  <img width="740" height="383" alt="image" src="https://github.com/user-attachments/assets/0b651d91-ddf9-497e-9ef0-3b047865e0e8" />
  <br/>
  <img width="1731" height="880" alt="image" src="https://github.com/user-attachments/assets/dc03192b-1234-498b-9990-ad5d543dadcc" />
  <img width="1920" height="1080" alt="Screenshot (121)" src="https://github.com/user-attachments/assets/c4f5976d-5306-4d0d-b249-8cac1f1f0e76" />
  <img width="1741" height="869" alt="Screenshot 2025-10-01 205737" src="https://github.com/user-attachments/assets/abca1667-4fde-4ce0-9738-f1e4373087c4" />
  <img width="1810" height="905" alt="Screenshot 2025-10-01 210010" src="https://github.com/user-attachments/assets/a1f8e9c0-01cb-4f03-8d09-a6e53d6bbf62" />
  <img width="1796" height="825" alt="Screenshot 2025-10-01 210028" src="https://github.com/user-attachments/assets/512fd553-1eb4-43f4-a780-17fa5286bf24" />
  <img width="1752" height="877" alt="Screenshot 2025-10-01 210119" src="https://github.com/user-attachments/assets/708d073e-7d90-429f-aadb-820d8acf21e9" />
  <img width="1723" height="875" alt="Screenshot 2025-10-01 210208" src="https://github.com/user-attachments/assets/d2a1366c-21a3-4c7b-8b6c-59feec1feced" />

  







