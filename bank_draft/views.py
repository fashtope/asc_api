from rest_framework import generics
from django_filters import rest_framework as filters
from bank_draft.filters import BankDraftFilter

from bank_draft.models import Bank, BankDraft
from bank_draft.serializers import BankDraftSerializer, BankSerializer


class BankView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
class BankDetailView(generics.RetrieveUpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    
class BankDraftView(generics.ListCreateAPIView):
    queryset = BankDraft.objects.all()
    serializer_class = BankDraftSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BankDraftFilter
    
    
class BankDraftDetailView(generics.RetrieveUpdateAPIView):
    queryset = BankDraft.objects.all()
    serializer_class = BankDraftSerializer