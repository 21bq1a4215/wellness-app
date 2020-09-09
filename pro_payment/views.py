from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response

from videos.models import Pricing

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class EnrollView(generic.TemplateView):
    """
    This function loads the main page to enrroll user 
    on subscription
    """
    template_name = "pro_payment/enroll.html"


class PaymentView(generic.TemplateView):
    """
    Payment and checkout view
    """
    template_name = 'pro_payment/checkout_pro.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        pricing = get_object_or_404(Pricing, slug=self.kwargs["slug"])
        context.update({
            "pricing_tier": pricing,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateSubscriptionView(APIView):
    """
    This function will create the subscription for the user
    some of the logic here is taken from stripe
    """
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=data['customerId'],
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer=data['customerId'],
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=data['customerId'],
                items=[{'price': 'price_HGd7M3DV3IMXkC'}],
                expand=['latest_invoice.payment_intent'],
            )

            data = {}
            data.update(subscription)

            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })


class RetryInvoiceView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.stripe_customer_id
        try:

            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            invoice = stripe.Invoice.retrieve(
                data['invoiceId'],
                expand=['payment_intent'],
            )
            data = {}
            data.update(invoice)

            return Response(data)
        except Exception as e:

            return Response({
                "error": {'message': str(e)}
            })
            
