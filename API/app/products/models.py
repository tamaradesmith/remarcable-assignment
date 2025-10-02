from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=250)

  class Meta:
    ordering = ['name']
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=30)
  
  class Meta:
    ordering = ['name']
    verbose_name_plural = "Tags"

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=250, db_index=True)
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.PROTECT)
  tag = models.ManyToManyField(Tag, blank=True)
  
  class Meta:
    ordering = ['category', 'name']
    db_table = 'product'
    verbose_name_plural = "products"
    indexes = [
      models.Index(fields=['category', 'name']),
    ]
  
  def __str__(self):
    return self.name
