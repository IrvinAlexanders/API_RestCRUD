from rest_framework import mixins, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated #Permisos

from .serializers import ProductModelSerializer

from .models import Product


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    #permission_classes = [IsAuthenticated]