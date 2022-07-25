from rest_framework import serializers

from bank_draft.models import Bank, BankDraft


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
        
        
class BankDraftSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankDraft
        fields='__all__'
        read_only_fields = ['date']
        
    # def validate_bank(self, value):
        