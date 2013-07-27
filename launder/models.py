from django.db import models

class WashFoldOrder(models.Model):

	PAYMENT_METHODS = (
		('CASH', 'Cash'),
		('CREDIT', 'Credit'),
		('CHECK', 'Check')
	)

	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	phone_number = models.CharField(max_length=15, blank=False)
	address = models.CharField(max_length=50, blank=False)
	date = models.DateTimeField(auto_now_add=True)
	total_cost = models.DecimalField(max_digits=5, decimal_places=2)
	payment_method = models.CharField(max_length=6, choices=PAYMENT_METHODS)
	payment_finalized = models.BooleanField()

class DryCleaning(models.Model):

	PAYMENT_METHODS = (
		('CASH', 'Cash'),
		('CREDIT', 'Credit'),
		('CHECK', 'Check')
	)

	GARMENT_OPTIONS = (
		('TROUSERS', 'Trousers'),
		('M SUITS', 'M Suits'),
		('TOP O COAT', 'Top O Coat'),
		('SHIRTS', 'Shirts'),
		('SPORTS COATS', 'Sports Coats'),
		('NECKTIES', 'Neckties - Hats'),
		('SWEATERS', 'Sweaters'),
		('DRESS', 'Dress'),
		('SKIRTS', 'Skirts'),
		('L SUITS', 'L Suits'),
		('BLOUSE', 'Blouse'),
		('TOP 3/4 COAT', 'Top 3/4 Coat'),
		('CAR COAT', 'Car Coat'),
		('SLACKS', 'Slacks')
	)

	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	phone_number = models.CharField(max_length=15, blank=False)
	address = models.CharField(max_length=50, blank=False)
	date = models.DateTimeField(auto_now_add=True)
	garment_type = models.TextField(max_length=12, choices=GARMENT_OPTIONS)
	garment_amount = models.IntegerField()
	total_cost = models.DecimalField(max_digits=5, decimal_places=2)
	payment_method = models.CharField(max_length=6, choices=PAYMENT_METHODS)
	payment_finalized = models.BooleanField()

class LaundryShirtsOrder(models.Model):

	PAYMENT_METHODS = (
		('CASH', 'Cash'),
		('CREDIT', 'Credit'),
		('CHECK', 'Check')
	)

	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50, blank=False)
	last_name = models.CharField(max_length=50, blank=False)
	phone_number = models.CharField(max_length=15, blank=False)
	address = models.CharField(max_length=50, blank=False)
	date = models.DateTimeField(auto_now_add=True)
	shirts_amount = models.IntegerField()
	shirts_price = models.DecimalField(max_digits=5, decimal_places=2)
	starched = models.BooleanField()
	total_cost = models.DecimalField(max_digits=5, decimal_places=2)
	payment_method = models.CharField(max_length=6, choices=PAYMENT_METHODS)
	payment_finalized = models.BooleanField()