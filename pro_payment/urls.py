from django.urls import path
from .views import PaymentView


app_name = "pro_payment"

urlpatterns = [
    path("", PaymentView.as_view(), name='payment'),
]