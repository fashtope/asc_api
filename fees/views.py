from rest_framework import generics
from django_filters import rest_framework as filters

from .filters import FeesFilter
from .models import Fees
from .serializers import FeesSerializer



class FeesView(generics.ListCreateAPIView):
    queryset = Fees.objects.all()
    serializer_class = FeesSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = FeesFilter


class FeesDetailView(generics.RetrieveAPIView):
    queryset = Fees.objects.all()
    serializer_class = FeesSerializer