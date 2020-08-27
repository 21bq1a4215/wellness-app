from django.urls import path
from . import views
from .webhooks import webhook
from .views import add_coupon

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('add-coupon/', add_coupon, name='add-coupon'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]