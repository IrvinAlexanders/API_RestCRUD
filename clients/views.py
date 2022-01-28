from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated

from .serializers import ClientModelSerializer

from .models import Client

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
    permission_classes = [IsAuthenticated]
#Método de ruta
@api_view(['GET'])
def read_csv(request):
#Añadir clientes desde archivo CSV
    file =  BASE_DIR / 'SIMULATED.csv'

    with open(file, mode='r') as f:
        clients = csv.DictReader(f)
        for row in clients:
            client = Client(**row)
            client.save()
            print(client.first_name)
    return Response(status=status.HTTP_201_CREATED)