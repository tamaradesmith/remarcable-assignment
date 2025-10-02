from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Tag, Product

class ProductAPITest(TestCase):
  def setUp(self):
    category = Category.objects.create(name="Category A")
    tag1 = Tag.objects.create(name="Tag 1")
    tag2 = Tag.objects.create(name="Tag 2")
    product = Product.objects.create(
      name="Product 1",
      description="A sample product",
      category=category
    )
    product.tag.set([tag1, tag2])
    self.client = Client()

  def test_index_route(self):
    url = reverse('all_products')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
      
  def test_get_product_route(self):
    category = Category.objects.create(name="Category A")
    tag1 = Tag.objects.create(name="Tag 1")
    product = Product.objects.create(
        name="Product 1",
        description="A sample product",
        category=category
    )
    product.tags.set([tag1])
  
    url = reverse('get_product', kwargs={'product_id': product.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
