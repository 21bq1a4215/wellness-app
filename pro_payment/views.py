from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentView(generic.TemplateView):
    template_name = 'pro_payment/checkout_pro.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateSubscriptionView(generic.View):
    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.stripe_customer_id
        try:
            # Attach the payment method to the customer
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

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': data["priceId"]}],
                expand=['latest_invoice.payment_intent'],
            )
            data = {}
            data.update(subscription)

            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({
                "error": {'message': str(e)}
            })


class RetryInvoiceView(generic.View):
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

            return JsonResponse(data)
        except Exception as e:

            return JsonResponse({
                "error": {'message': str(e)}
            })
