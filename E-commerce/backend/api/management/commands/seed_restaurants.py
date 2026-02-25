import random
from django.core.management.base import BaseCommand
from faker import Faker
from api.models import Restaurant, Product
from django.core.files import File
from django.conf import settings
from pathlib import Path

fake = Faker()

class Command(BaseCommand):
    help = "Seed restaurants with mock data"

    def handle(self, *args, **kwargs):
        images_path = Path(settings.BASE_DIR) / "seed_images"
        images = list(images_path.glob("*.jpg"))

        if not images:
            self.stdout.write(self.style.ERROR("No images found in seed_images"))
            return

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
