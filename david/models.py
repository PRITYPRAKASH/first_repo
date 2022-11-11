from itertools import product
from statistics import quantiles
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



class David(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

PRODUCT_CHOICES=(
  ('TV','tv'),
  ('IPAD','ipad'),
  ('PLAYSTATION','playstation')
)
class sale(models.Model):
  product=models.CharField(max_length=500,choices=PRODUCT_CHOICES)
  salesman=models.ForeignKey(User,on_delete=models.CASCADE)
  quantity=models.PositiveBigIntegerField()
  total=models.FloatField(blank=True)
  updated=models.DateTimeField(auto_now=True)
  created=models.DateTimeField(auto_now_add=True)

  def __str__(self) :
     return f"{self.product}-{self.quantity}"

  def save(self,*args, **kwargs):
    price =None
    if self.product=='TV':
      price=559.99
    elif self.product=='IPAD':
      price=400.00
    elif self.product=='PLAYSTATION':
      price=466.99
    else:
      pass
    self.total=price * self.quantity
    super().save(*args, **kwargs)
