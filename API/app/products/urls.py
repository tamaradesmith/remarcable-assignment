from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='all_products'),
  path('product_filter_options', views.index_filter_options, name='product_filter_options'),
  path('<int:product_id>/', views.get, name='get_product'),
]