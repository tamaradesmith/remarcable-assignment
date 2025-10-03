from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='all_products'),
  path('<int:product_id>/', views.get, name='get_product'),
]