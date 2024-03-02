from rest_framework  import viewsets
from  .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):  #used for listing a product from a model.
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     lookup_field = 'pk'
