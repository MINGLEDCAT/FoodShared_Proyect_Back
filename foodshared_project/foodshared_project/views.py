from rest_framework import generics
from .models import Alimentos
from .serializers import AlimentosSerializer

class AlimentosListCreate(generics.ListCreateAPIView):
    queryset = Alimentos.objects.all()
    serializer_class = AlimentosSerializer
