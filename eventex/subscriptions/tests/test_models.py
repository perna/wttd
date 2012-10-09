#coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name = 'Anderson Meira',
			cpf = '12345678901',
			email = 'andersonmeira@outlook.com',
			phone = '14-91010101'
		)

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1,self.obj.id)


	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at,datetime)

	def test_unicode(self):
		self.assertEqual(u'Anderson Meira',unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		#Create a firs entry to force colision
		Subscription.objects.create(name='Anderson Meira', cpf='1234567890',
									email ='andersonmeira@outlook.com', phone='14-91010101')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Anderson Meira', cpf='1234567890',
									email ='andersonmeira@outlook.com', phone='14-91010101')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique'
		s = Subscription(name='Anderson Meira', cpf='0234567890',
									email ='andersonmeira@outlook.com', phone='14-91010101')
		self.assertRaises(IntegrityError, s.save)
