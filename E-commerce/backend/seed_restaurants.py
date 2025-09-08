import random
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Restaurant, Product
from django.core.files import File
from pathlib import Path

fake = Faker()

class Command(BaseCommand):
    help = "Seed restaurants with mock data"

    def handle(self, *args, **kwargs):
        images_path = Path("seed_images")  # folder with stock images

        for _ in range(10):  # create 10 restaurants
            restaurant = Restaurant.objects.create(
                name=fake.company(),
                description=fake.text(),
            )
            image_file = random.choice(list(images_path.glob("*.jpg")))
            restaurant.image.save(image_file.name, File(open(image_file, "rb")))

            # add products
            for _ in range(5):
                Product.objects.create(
                    restaurant=restaurant,
                    name=fake.word().title(),
                    description=fake.sentence(),
                    price=random.randint(1000, 5000) / 100,  # NGN 10–50
                )
