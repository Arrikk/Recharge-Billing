from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.timezone import now

# Create your models here.


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(default = "NGN", max_length=50, null=True, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=8, default='0.00')
    created_at  = models.DateTimeField(default = now, blank=True)
    # transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)

    
class Deposite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    # currency = models.CharField(default = "NGN", max_length=50, null=True, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=8, default='0.00')
    # date  = models.DateTimeField(timezone.now, blank=True)
    created_at  = models.DateTimeField(default = now, blank=True)

    # transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    
class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    # currency = models.CharField(default = "NGN", max_length=50, null=True, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=8, default='0.00')
    created_at  = models.DateTimeField(default=now, blank=True)
    # date  = models.DateTimeField(timezone.now, blank=True)
    
    # transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    
class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    sent_to = models.CharField(max_length=250, blank=True, null=True)
    # currency = models.CharField(default = "NGN", max_length=50, null=True, blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=8, default='0.00')
    created_at  = models.DateTimeField(default = now, blank=True)
    # date  = models.DateTimeField(timezone.now, blank=True)
    # transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    

class Transaction(models.Model):
    # TRANSACTIONS = (
    #     ('deposite', 'deposite'),
    #     ('transfer', 'transfer'),
    #     ('withdraw', 'withdraw'),
    # )
    # wallet = models.ForeignKey("wallet", on_delete=models.CASCADE)
    # transaction_type = models.CharField(max_length=250, choices=TRANSACTIONS, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    sent_to = models.CharField(max_length=250, blank=True, null=True)
    transaction_type = models.CharField(max_length=250, null=True, blank=True)
    balance_before = models.DecimalField(max_digits=8, decimal_places=2)
    balance_after = models.DecimalField(max_digits=8, decimal_places=2)
    created_at  = models.DateTimeField(default=now, blank=True)
    status = models.CharField(max_length=50, blank=True, default='pending')
    paystack_payment_reference = models.CharField(max_length=250, default='', blank=True, null=True)
    # created_at = models.DateTimeField(timezone.now, blank=True)
    
    # deposite = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.name} made a {self.transaction_type} on {self.created_at}"
