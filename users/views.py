from rest_framework import mixins, viewsets,status
from rest_framework.decorators import action 
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User

from .serializers import UserModelSerializer, UserSignUpSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self): #Asignando permisos
       
        if self.action in ['signup']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def signup(self, request): #Reegistro de usuarios
    
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)