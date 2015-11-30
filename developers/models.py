from django.db import models
import datetime
#from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from django.forms import TextInput
from django.utils import timezone
from django.db.models import signals
from django.contrib.auth.models import User,Group
from django.template.defaultfilters import date
from django.core.urlresolvers import reverse
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField

def upload_profile(instance, filename):
   # return "title_images/%s" % (filename)
	return '/'.join(['profilephoto', str(instance.idnumber), filename])

def upload_job(instance, filename):
	return "job_images/%s" % (filename)

# Create your models here.
categories =  (
	('Java', 'Java'),
	('Python', 'Python'),
	('C#', 'C#'),
	('Ruby', 'Ruby'),
	('JavaScript', 'JavaScript'),

	)
available = (
	('Part Time','Part Time'),
	('Full Time', 'Full Time')
	)

jobs = (
	('Hardware','Hardware'),
	('Software', 'Software'),
	('Support','Support'),
	('Design','Design')
	)
description = (
	('Developer','Developer'),
	('Employer','Employer')
	)
class UserProfile(models.Model):
	
	user = models.OneToOneField(User)
	category = models.CharField(max_length=20,choices=description, default=description[0][0])
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires = models.DateTimeField(default=datetime.datetime.now)
	
	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural='User profiles'

class devQuerySet(models.QuerySet):
	def approved(self):
		return self.filter(approved=True)

class Developers(models.Model):
	name = models.CharField(max_length=50)
	idnumber = models.IntegerField()
	#photo = models.ImageField(upload_to=upload_profile,null=True, blank=True,)
	email = models.EmailField()
	telephone = PhoneNumberField()
	website = models.URLField()
	organization = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=50)
	location = PlainLocationField(based_fields=[city], zoom=7)
	category = models.CharField(max_length=50, choices = categories, default=categories[0][0])
	availability = models.CharField(max_length=50, choices = available, default=available[0][0])
	education = models.TextField()
	employment = models.TextField()
	date_applied = models.DateTimeField(auto_now_add=True)
	projects = models.TextField()
	skills = models.TextField()
	portfolio = models.TextField()
	slug = models.SlugField(max_length=200, unique=True, null=True)
	approved = models.BooleanField(default=False)
	available = models.BooleanField(default=True)
	objects = devQuerySet.as_manager()

	def __unicode__(self):
		return self.name

	def item_pubdate(self, item):
		return datetime.datetime(item.posted.year, item.posted.month, item.posted.day)

	def get_absolute_url(self):
		return reverse("developer_detail", kwargs={"slug": self.slug})

	def get_developers_count(self):
		return self.Developer.count()
		

	class Meta:
		verbose_name_plural = "Developers List" 
		managed = True

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug	
		

class Jobs(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	#picture = models.ImageField(upload_to=upload_job,null=True, blank=True,)
	tags = models.ManyToManyField(Tag)
	slug = models.SlugField(max_length=20,unique=True)
	category = models.CharField(max_length=50, choices=jobs, default=jobs[0][0])

	def __unicode__(self):
		return self.name
		

	class Meta:
		verbose_name_plural = "Jobs List" 
		managed = True

class Employer(models.Model):
	name = models.CharField(max_length=50)
	idnumber = models.IntegerField()
	email = models.EmailField()
	telephone = PhoneNumberField()
	website = models.URLField()
	organization = models.TextField()
	description = models.TextField()
	date_requested = models.DateTimeField(auto_now_add=True,null=True)

	def __unicode__(self):
		return self.name
		

	class Meta:
		verbose_name_plural = "Employers List" 
		managed = True
