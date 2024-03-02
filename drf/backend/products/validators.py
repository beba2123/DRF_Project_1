from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

def validate_title(value):
     qs = Product.objects.filter(title__iexact=value) # filter title that is similar to product title the reason iexact is to make sure it is more case sensetive.
     if qs.exists():
         raise serializers.ValidationError(f"A product with this {value} title already exists.")
     return value

def validate_title_no_hello(value):
     if "hello" in value.lower():
          raise serializers.ValidationError(f"A product with this {value} title already exists.")
     return value

unique_product_title = UniqueValidator(queryset=Product.objects.all())