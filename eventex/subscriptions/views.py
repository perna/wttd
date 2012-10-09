#coding: utf-8
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

def subscribe(request):
	if request.method == 'POST':
		form = SubscriptionForm(request.POST)
		form.is_valid()
		obj = Subscription(**form.cleaned_data)
		obj.save()
		return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
	else:
		return direct_to_template(request,
			'subscriptions/subscription_form.html',
			{'form':SubscriptionForm()})