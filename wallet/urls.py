from django.urls import path, re_path

from wallet.models import Transfer
from .views import (DepositeView, TransferView, VerifyDepositeView, 
                    WalletCreateView,
                    WalletTransaction,
                    WithdrawView)


urlpatterns = [
    path('create/', WalletCreateView.as_view()),
    path('transaction/', WalletTransaction.as_view()),
    path('deposite/', DepositeView.as_view()),
    path('deposit/verify/<str:reference>/', VerifyDepositeView.as_view()),
    path('withdraw/', WithdrawView.as_view()),
    path('transfer/', TransferView.as_view()),
]