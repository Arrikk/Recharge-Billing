from dataclasses import fields
from rest_framework import serializers
from .models import (
    Transaction,
    User,
    Wallet,
    # Deposite
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'balance']

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('__all__')
        
        
class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Transaction
        fields = ('__all__')
        
# class DepositeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposite
#         fields = ('__all__')