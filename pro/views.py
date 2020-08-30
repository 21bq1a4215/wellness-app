from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import stripe
import json


def pro(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HL7iOHeew9pZh4Qb0TUOSN4',
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://8000-cc83ffdc-8eed-493d-a6f1-9ec57a9ec108.ws-eu01.gitpod.io/thanks' + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://8000-cc83ffdc-8eed-493d-a6f1-9ec57a9ec108.ws-eu01.gitpod.io/pro',
    )

    context = {
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'pro/pro.html', context)

def thanks(request):
    return render(request, 'pro/thanks.html')

@login_required(login_url='/accounts/login/')
def pro_members(request):
    return render(request, 'pro/pro-members.html')
