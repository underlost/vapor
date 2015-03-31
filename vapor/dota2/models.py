from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode, smart_str
from django.utils.translation import ugettext_lazy as _

class Hero(models.Model):
	name = models.CharField(max_length=255)
	localized_name = models.CharField(max_length=355)
	date_last_updated = models.DateTimeField(null=True, blank=True)
	
	class Meta:
	    db_table = 'dota2_heroes'
	    verbose_name_plural = 'Heroes'
	    
	def __unicode__(self):
	    return self.name
	    
class Ability(models.Model):
	name = models.CharField(max_length=255)
	localized_name = models.CharField(max_length=355)
	date_last_updated = models.DateTimeField(null=True, blank=True)

	class Meta:
	    db_table = 'dota2_abilities'
	    verbose_name_plural = 'Abilities'
	    
	def __unicode__(self):
	    return self.name

class Item(models.Model):
	name = models.CharField(max_length=255)
	localized_name = models.CharField(max_length=355)
	date_last_updated = models.DateTimeField(null=True, blank=True)

	class Meta:
	    db_table = 'dota2_items'
	    verbose_name_plural = 'Items'
	    
	def __unicode__(self):
	    return self.name