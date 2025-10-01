import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from moviemate.models import StreamPlatform, WatchList, Review


class Command(BaseCommand):
    help = "Seed database with sample users, movies (watchlist), and reviews"

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Starting database seeding...")

        # Create admin user
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("✅ Admin user created."))

        # Create 50 normal users
        for i in range(1, 51):
            username = f"user{i}"
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password="pass1234")
        self.stdout.write(self.style.SUCCESS("✅ 50 users created."))

        # Create streaming platforms
        platforms = [
            {"name": "Netflix", "about": "Popular streaming platform", "website": "https://netflix.com"},
            {"name": "Amazon Prime", "about": "Prime streaming service", "website": "https://primevideo.com"},
            {"name": "Disney+", "about": "Disney streaming service", "website": "https://disneyplus.com"},
            {"name": "HBO Max", "about": "HBO streaming service", "website": "https://hbomax.com"},
            {"name": "Hulu", "about": "Streaming platform", "website": "https://hulu.com"},
        ]
        for p in platforms:
            StreamPlatform.objects.get_or_create(name=p["name"], about=p["about"], website=p["website"])
        self.stdout.write(self.style.SUCCESS("✅ Platforms created."))

        # Create 120 movies (WatchList entries)
        platform_objs = list(StreamPlatform.objects.all())
        for i in range(1, 121):
            WatchList.objects.get_or_create(
                title=f"Movie {i}",
                storyline=f"Storyline for movie {i}",
                active=True,
                platform=random.choice(platform_objs),
            )
        self.stdout.write(self.style.SUCCESS("✅ 120 movies created."))

        # Create ~5000 reviews
        users = list(User.objects.filter(is_superuser=False))
        watchlist_objs = list(WatchList.objects.all())

        review_count, target_reviews = 0, 5000

        while review_count < target_reviews:
            movie = random.choice(watchlist_objs)
            user = random.choice(users)

            # Ensure one review per user per movie
            if not Review.objects.filter(watchlist=movie, review_user=user).exists():
                Review.objects.create(
                    review_user=user,
                    rating=random.randint(1, 10),
                    description=f"Review by {user.username} for {movie.title}",
                    watchlist=movie,
                    active=True,
                )
                review_count += 1
                if review_count % 500 == 0:
                    self.stdout.write(self.style.WARNING(f"⚡ {review_count} reviews created..."))

        self.stdout.write(self.style.SUCCESS("🎉 5000 reviews created."))
        self.stdout.write(self.style.SUCCESS("✅ Seeding completed successfully!"))
