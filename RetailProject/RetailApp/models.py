from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	product_cat=models.ForeignKey('Category',on_delete=models.CASCADE)
	product_id=models.CharField(max_length=50,primary_key=True)
	product_name=models.CharField(max_length=100)
	product_prize=models.CharField(max_length=50)
	product_discription=models.CharField(max_length=200)
	class Meta:
		db_table='Product' 

	def __str__(self):
		return self.product_id

class Customer(models.Model):
	customer_id=models.CharField(max_length=50)
	customer_name=models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	class Meta:
		db_table='Customer' 

	def __str__(self):
		return self.customer_id

class Category(models.Model):
	product_cat=models.CharField(max_length=50)
	class Meta:
		db_table='Category'

	def __str__(self):
		return self.product_cat


