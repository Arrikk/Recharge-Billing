from django.contrib import admin

from wallet.models import Deposite, Transaction, Transfer, Wallet, Withdraw

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Deposite)
admin.site.register(Transaction)
admin.site.register(Withdraw)
admin.site.register(Transfer)
