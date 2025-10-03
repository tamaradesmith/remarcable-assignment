from  django.core.management.base import BaseCommand
from app.products.models import Category, Product, Tag

class Command(BaseCommand):
  help = "Seed categories, tags and products into the database"
  
  def handle(self):
    categories = ["Cat Food", "Cat Treats", "Cat Toys", "Cat Beds", "Cat Accessories", "Cat Health"]
    tags = ["Organic", "Premium", "Cheap", "Indoor", "Outdoor", "Kitten", "Adult", "Luxury", "Toy", "Food"]
    products = [
      {"name": "Salmon Kibble", "category": "Cat Food"},
      {"name": "Chicken Pâté", "category": "Cat Food"},
      {"name": "Tuna Treats", "category": "Cat Food"},
      {"name": "Feather Wand", "category": "Cat Toys"},
      {"name": "Laser Pointer", "category": "Cat Toys"},
      {"name": "Catnip Mouse", "category": "Cat Toys"},
      {"name": "Cozy Cave", "category": "Cat Beds"},
      {"name": "Window Perch", "category": "Cat Beds"},
      {"name": "Heated Mat", "category": "Cat Beds"},
      {"name": "Collar with Bell", "category": "Cat Accessories"},
      {"name": "Scratching Post", "category": "Cat Accessories"},
      {"name": "Grooming Brush", "category": "Cat Accessories"},
      {"name": "Vitamin Supplements", "category": "Cat Health"},
      {"name": "Dental Chews", "category": "Cat Health"},
      {"name": "Flea Collar", "category": "Cat Health"},
      {"name": "Interactive Ball", "category": "Cat Toys"},
      {"name": "Cat Tunnel", "category": "Cat Toys"},
      {"name": "Premium Wet Food", "category": "Cat Food"},
      {"name": "Kitten Milk", "category": "Cat Food"},
      {"name": "Luxury Cat Bed", "category": "Cat Beds"},
      {"name": "Salmon Bites", "category": "Cat Treats"},
      {"name": "Chicken Chews", "category": "Cat Treats"},
      {"name": "Tuna Crunchies", "category": "Cat Treats"},
    ]
    
    category_objs = {}
    for name in categories:
      obj, created = Category.objects.get_or_create(name=name)
      category_objs[name] = obj
      
      if created:
        self.stdout.write(self.style.SUCCESS(f"Created category: {name}"))
      else:
        self.stdout.write(self.style.WARNING(f"Category already exists: {name}"))
      
    tag_objs = {}
    for name in tags:
      obj, created = Tag.objects.get_or_create(name=name)
      tag_objs[name]= obj
      
      if created:
        self.stdout.write(self.style.SUCCESS(f"Created tag: {name}"))
      else:
        self.stdout.write(self.style.WARNING(f"Tag already exists: {name}"))
        
    products = {
      "Cat Food": [
        {"name": "Salmon Kibble", "tags": ["Premium", "Food"]},
        {"name": "Chicken Pâté", "tags": ["Organic", "Food"]},
        {"name": "Tuna Wet Food", "tags": ["Cheap", "Food"]},
        {"name": "Premium Dry Food", "tags": ["Premium", "Luxury"]}
      ],
      "Cat Treats": [
        {"name": "Salmon Bites", "tags": ["Premium"]},
        {"name": "Chicken Chews", "tags": ["Cheap"]},
        {"name": "Tuna Crunchies", "tags": ["Food"]},
        {"name": "Cheese Nibbles", "tags": []}
      ],
      "Cat Toys": [
        {"name": "Feather Wand", "tags": ["Toy"]},
        {"name": "Laser Pointer", "tags": ["Indoor", "Toy"]},
        {"name": "Catnip Mouse", "tags": ["Toy"]},
        {"name": "Interactive Ball", "tags": ["Indoor"]},
        {"name": "Cat Tunnel", "tags": ["Indoor", "Outdoor"]}
      ],
      "Cat Beds": [
        {"name": "Cozy Cave", "tags": ["Indoor"]},
        {"name": "Window Perch", "tags": ["Indoor"]},
        {"name": "Heated Mat", "tags": ["Luxury"]},
        {"name": "Luxury Cat Bed", "tags": ["Luxury"]}
      ],
      "Cat Accessories": [
        {"name": "Collar with Bell", "tags": ["Luxury"]},
        {"name": "Scratching Post", "tags": ["Indoor"]},
        {"name": "Grooming Brush", "tags": []},
        {"name": "Harness and Leash", "tags": ["Outdoor"]}
      ],
      "Cat Health": [
        {"name": "Vitamin Supplements", "tags": ["Premium"]},
        {"name": "Dental Chews", "tags": ["Food"]},
        {"name": "Flea Collar", "tags": ["Premium"]},
        {"name": "Kitten Milk", "tags": ["Kitten"]}
      ]
    }
    
    for catgory_name, items in products.items():
      category = category_objs[catgory_name]
      
      for item in items:
        prod, created = Product.objects.get_or_create(
          name=item["name"],
          category=category
        )
      
        tag_objs_to_assign = [tag_objs[tag_name] for tag_name in item["tags"] if tag_name in tag_objs]
        prod.tag.set(tag_objs_to_assign)
        prod.save()
        
        if created:
          self.stdout.write(self.style.SUCCESS(f"Created product: {item['name']}"))
        else:
          self.stdout.write(self.style.WARNING(f"Product already exists: {item['name']}"))
        
    self.stdout.write(self.style.SUCCESS("Seeding complete!"))