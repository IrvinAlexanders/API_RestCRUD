from rest_framework import mixins, viewsets
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from .serializers import BillModelSerializer, BillProductsSerializer

from .models import Bill, BillProducts


class BillViewSet(viewsets.ModelViewSet):

    queryset = Bill.objects.all()
    serializer_class = BillModelSerializer
    permission_classes = [IsAuthenticated]

class BillProductsViewSet(viewsets.ModelViewSet):
    
    queryset = BillProducts.objects.all()
    serializer_class = BillProductsSerializer
    permission_classes = [IsAuthenticated]
