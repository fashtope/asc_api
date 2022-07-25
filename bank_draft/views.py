from rest_framework import generics

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
    
    
class BankDraftDetailView(generics.RetrieveUpdateAPIView):
    queryset = BankDraft.objects.all()
    serializer_class = BankDraftSerializer