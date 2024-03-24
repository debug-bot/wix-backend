from django.db import models
# get User model
from django.contrib.auth import get_user_model
from django.utils import timesince

User = get_user_model()

# Create your models here.

# This is to know the props of the product variations
SUBTAGS_CHOICES = (
    ('ARRIBA', 'ARRIBA'),
    ('ABAJO', 'ABAJO'),
    ('VESTIDO', 'VESTIDO'),
    ('ACCESORIO', 'ACCESORIO'),
)

EXTRA_TAG_CHOICES = (
    ('WOMEN', 'WOMEN'),
    ('MEN', 'MEN'),
    ('KIDS', 'KIDS'),
)

DISCOUNT_CHOICES = (
    ('POR CIENTO', 'POR CIENTO'),
    ('FIJO', 'FIJO'),
)

COLLECTION_CHOICES = (
    ('Luxury', 'Luxury'),
    ('Etnik', 'Etnik'),
)
class CustomColor(models.Model):
	title = models.CharField(max_length=256, default='', )
	code = models.CharField(max_length=256, default='')

	def __str__(self):
		return self.code + " - " + self.title

class CustomCollection(models.Model):
	title = models.CharField(max_length=256, choices=COLLECTION_CHOICES, default='Luxury')
	description = models.TextField(blank=True)
	image = image = models.ImageField(upload_to='uploads/collections/', blank=True, null=True)

	def all_products_per_collection(self):
		return self.products_per_collection_set.all()

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=256, default='')
	image = models.ImageField(upload_to='uploads/categories/', blank=True)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length=256, default='')
	code = models.CharField(max_length=256, default='')
	price = models.FloatField(default=0.0)
	image = models.ImageField(upload_to='uploads/products/', blank=True)
	s_image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
	amount_sold = models.IntegerField(default=0)
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name="product_set")
	subtag = models.CharField(max_length=256, choices=SUBTAGS_CHOICES, default='ARRIBA')
	available_colors = models.ManyToManyField(CustomColor)
	collection = models.ManyToManyField(CustomCollection, related_name='products_per_collection_set')
	description = models.TextField(blank=True)
	extra_tag = models.CharField(max_length=256, choices=EXTRA_TAG_CHOICES, default='WOMEN')

	def __str__(self):
		return self.title + " - " + self.category.title + " - " + self.subtag


class ProductImage(models.Model):
	image = models.ImageField(upload_to='uploads/products-images/', blank=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	type = models.CharField(max_length=256, default='first')

	def __str__(self):
		return self.product.title



class Cart(models.Model):
	ip_address = models.GenericIPAddressField()
	cost = models.FloatField(default=0)
	last = models.BooleanField(default=False)
	token = models.CharField(max_length=256, default='-1')

	def __str__(self):
		return self.ip_address + " - " + self.token

class ProductVariation(models.Model):
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	cant = models.IntegerField(default=1)
	cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE, related_name="product_variation_set")
	price = models.FloatField(default=0)
	clothing_s = models.CharField(max_length=256, default="S")
	size_of_sleeve = models.CharField(max_length=256, default="Corta")
	fit = models.CharField(max_length=256, default="Regular Fit")
	color = models.CharField(max_length=256, default="Default")

	def __str__(self):
		if self.product is not None:
			return self.product.title
		else:
			return "No product can be viewed now"


class Payment(models.Model):
	ip_address = models.GenericIPAddressField()
	email = models.CharField(max_length=256, default='-1')
	stripe_charge_id = models.CharField(max_length=50)
	amount = models.FloatField(default=0.0)
	timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	refund = models.CharField(max_length=256, default="No refund asked")

	def __str__(self):
		if ((self.email != "") and (self.email != '-1')):
			return self.email + " - " + self.timestamp.strftime("%b. %-d, %Y, %-I:%M %p")
		else:
			return str(self.ip_address) + " - " + self.timestamp.strftime("%b. %-d, %Y, %-I:%M %p")



class Order(models.Model):
	cart = models.ForeignKey(Cart, null=True, on_delete=models.SET_NULL, blank=True)
	email = models.CharField(max_length=256, default='-1')
	phone = models.CharField(max_length=256, default='-1')
	address1 = models.CharField(max_length=256, default='-1')
	address2 = models.CharField(max_length=256, default='-1')
	user_first_name = models.CharField(max_length=256, default='-1')
	user_last_name = models.CharField(max_length=256, default='-1')
	ordered_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
	ordered = models.BooleanField(default=False)
	status = models.CharField(max_length=256, default="Ordered")
	payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		if ((self.email != "") and (self.email != '-1')):
			return self.email + '-' + self.ordered_date.strftime("%b. %-d, %Y, %-I:%M %p")
		else:
			return self.user_first_name + " " + self.user_last_name + " - " + self.ordered_date.strftime("%b. %-d, %Y, %-I:%M %p")

	def get_total_price(self):
		return self.cart.cost

class Coupon(models.Model):
	user_email = models.CharField(max_length=256, default='')
	code = models.CharField(max_length=256, default='')
	taken = models.BooleanField(default=False)
	cart = models.ForeignKey(Cart, null=True, on_delete=models.SET_NULL,blank=True)
	discount_type = models.CharField(max_length=256, choices=DISCOUNT_CHOICES, default='POR CIENTO')
	discount = models.FloatField(default=0.0)
	how_many_items = models.IntegerField(default=0)

	def __str__(self):
		return self.user_email + " - " + self.code


class WebsiteTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section1 = models.TextField(blank=True, null=True)
    section2 = models.TextField(blank=True, null=True)
    section3 = models.TextField(blank=True, null=True)
    section4 = models.TextField(blank=True, null=True)
    section5 = models.TextField(blank=True, null=True)
    section6 = models.TextField(blank=True, null=True)
    section7 = models.TextField(blank=True, null=True)
    section8 = models.TextField(blank=True, null=True)
    
    def __str__(self):
    	return "Website Template"
    
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
class Templates(models.Model):
	image = models.ImageField(upload_to='templates/', blank=True, null=True)
	title = models.CharField(max_length=256, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	html_content = models.TextField(blank=True, null=True)
	html_content1 = models.TextField(blank=True, null=True)
	html_content2 = models.TextField(blank=True, null=True)
	html_content3 = models.TextField(blank=True, null=True)
	css_cotent = models.TextField(blank=True, null=True)
	js_content = models.TextField(blank=True, null=True)
	ecommerce = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
	
	class Meta:
		ordering = ['-created_at']
	
	def __str__(self):
	    return "Template " + self.title + " " + str(self.id)


class UserTemplate(models.Model):
	user = models.ForeignKey(User, related_name='templates', on_delete=models.CASCADE)
	template = models.ForeignKey(Templates, related_name="user_templates", on_delete=models.CASCADE)
	title = models.CharField(max_length=256, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	html_content = models.TextField(blank=True, null=True)
	html_content1 = models.TextField(blank=True, null=True)
	html_content2 = models.TextField(blank=True, null=True)
	html_content3 = models.TextField(blank=True, null=True)
	css_cotent = models.TextField(blank=True, null=True)
	js_content = models.TextField(blank=True, null=True)
	ecommerce = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def time_since_updated(self):
		return timesince.timesince(self.updated_at)

	def copy_template(self):
		"""
		Copies the relevant data from the linked template.
		"""
		self.title = self.template.title
		self.description = self.template.description
		self.html_content = self.template.html_content
		self.css_cotent = self.template.css_cotent
		self.js_content = self.template.js_content
		self.html_content1 = self.template.html_content1
		self.html_content2 = self.template.html_content2
		self.html_content3 = self.template.html_content3
		self.ecommerce = self.template.ecommerce
  
	def save(self, *args, **kwargs):
		"""
		Overriding the save method to copy template data on creation.
		"""
		if not self.pk:  # Check if it's a new instance
			self.copy_template()
		super(UserTemplate, self).save(*args, **kwargs)
  
	class Meta:
		ordering = ['-updated_at']


	def __str__(self):
		return "User Template " + self.time_since_updated() + " ago" + str(self.id)

 
    
class QrCodeHistory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)

	def time_since_updated(self):
		return timesince.timesince(self.created_at)

	def __str__(self):
		return f"{self.user.name}: {self.url}"