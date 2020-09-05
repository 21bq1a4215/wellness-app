from django.urls import path
from .views import PaymentView, CreateSubscriptionView, RetryInvoiceView


app_name = "pro_payment"

urlpatterns = [
    path("", PaymentView.as_view(), name='payment'),
    path('create-subscription/', CreateSubscriptionView.as_view(), name='create-subscription'),
    path('retry-invoice/', RetryInvoiceView.as_view(), name='retry-invoice'),
]