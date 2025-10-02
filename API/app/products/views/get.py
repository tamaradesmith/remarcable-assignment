from django.http import JsonResponse, Http404
from ..models import Product

def get(request, product_id):
  try:
    product = Product.objects.get(id=product_id)
  
  except Product.DoesNotExist:
    raise Http404("Product not found")
  
  data = {
    'id': product.id,
    'name': product.name,
    'categores': product.category.name,
    'description': product.description,
    'tags': [tag.name for tag in product.tag.all()]
  }
  
  return JsonResponse(data)