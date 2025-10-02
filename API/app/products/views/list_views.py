from django.http import JsonResponse
from ..models import Product

def index(request):
  products = Product.objects.all()
  
  data = [{
    'id': product.id,
    'name': product.name,
    'categores': product.category.name,
    'tags': [tag.name for tag in product.tag.all()]
  } for product in products]
  return JsonResponse({'products': data})