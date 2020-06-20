from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):

	name=models.CharField(max_length=250)
	contact=models.IntegerField(unique=True,blank=True)
	subject=models.CharField(max_length=250)
	message=models.TextField()

	def __str__(self):
		return self.name

class Statement(models.Model):

	month=models.CharField(max_length=20)
	year=models.CharField(max_length=10)
	nfsa_choice=(
		("NFSA","NFSA"),
		("APL","APL"),
		("MDM","MDM"),
		("PMGKY","PMGKY"),
		)
	rice_choice=(
		("RICE","RICE"),
		("WHEAT","WHEAT"),
		("DAL","DAL"),
		)
	type_scheme=models.CharField(max_length=20,choices=nfsa_choice,default="NFSA")
	type_grain=models.CharField(max_length=20,choices=rice_choice,default="RICE")
	os=models.IntegerField(default=0)
	uthan=models.IntegerField(default=0)
	vitran=models.IntegerField(default=0)
	agami=models.IntegerField(default=0)
	def __str__(self):
		return self.month

class Category(models.Model):
	cat_id=models.IntegerField(default=1)
	cat_name=models.CharField(max_length=50)
	cover_pic=models.FileField(upload_to="media")
	description=models.TextField()
	added_on=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.cat_name

class Register_table(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	contact_no=models.IntegerField(unique=True)

class Addproduct(models.Model):
	product_name=models.CharField(max_length=100)
	product_id=models.IntegerField(default=1)
	product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
	product_price=models.FloatField()
	sale_price=models.FloatField()
	product_image=models.ImageField(upload_to="products")
	details=models.TextField()

class Cout(models.Model):
	item=models.CharField(max_length=20)
	value_cart=models.CharField(max_length=2000)

class placeOrder(models.Model):
	name=models.CharField(max_length=250)
	contact=models.IntegerField(unique=True,blank=True)
	add=models.CharField(max_length=250)
	item=models.CharField(max_length=20)
	value_cart=models.CharField(max_length=2000)




# Create your models here.
