from django.http import JsonResponse
from django.db.models import Q
from ..models import Product, Tag, Category

def index(request):
  tags_param = request.GET.get("tags", "")
  categories_param = request.GET.get("catgories", "")
  search_param = request.GET.get("search", "")
  
  tags = [t.strip() for t in tags_param.split(",") if t.strip()]
  categories = [c.strip() for c in categories_param.split(",") if c.strip()]
  
  products = Product.objects.all().prefetch_related('tag')
  
  if categories:
    cat_q = Q()
    for cat_name in categories:
      cat_q |= Q(category__name__iexact=cat_name)
    products = products.filter(cat_q)

  if tags:
    q = Q()
    for tag_name in tags:
      q |= Q(tag__name__iexact=tag_name)
    products = products.filter(q).distinct()
    
  if search_param:
    products = products.filter(name__icontains=search_param)
  
  data = [{
    'id': product.id,
    'name': product.name,
    'category': product.category.name,
    'tags': [tag.name for tag in product.tag.all()]
  } for product in products]
  return JsonResponse({'products': data})

def index_filter_options(request):
  tags = Tag.objects.all()
  categories = Category.objects.all()
  
  tag_data = [tag.name for tag in tags]
  
  categories_data = [category.name for category in categories]
  
  return JsonResponse({'tags': tag_data, 'categories': categories_data})
