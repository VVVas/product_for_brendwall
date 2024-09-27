from rest_framework import mixins, viewsets

from products.models import Product

from .serializers import ProductSerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
