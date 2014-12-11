# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class PP_Podhod(models.Model):
	pp = models.CharField(max_length=2)
	name = models.CharField(max_length=30)

	def __unicode__ ( self ) :
		return self.name

class PP_Yprazneniya(models.Model):
	pp = models.CharField(max_length=1)
	name = models.CharField(max_length=30)

	def __unicode__ ( self ) :
		return self.name

class Vid_Podhod(models.Model):
	name = models.CharField(max_length=25)

	def __unicode__ ( self ) :
		return self.name

class Vid_Treni(models.Model):
	name = models.CharField(max_length=25)
	status = models.BooleanField(default=True)

	def __unicode__ ( self ) :
		return self.name

	class Meta :
		verbose_name    = u'Вид упражнения'
		verbose_name_plural  = u'Вид упражнений'
		ordering 		= [u'name']


class Zanyatie(models.Model):
	user   		   = models.ForeignKey(UserProfile)
	date 		   = models.DateField(default=datetime.now, blank=True)
	date_create    = models.DateTimeField(auto_now=True, blank=True)
	status 		   = models.BooleanField(default=True)

	def __unicode__ ( self ) :
		return str(self.id)




class Yprazneniya(models.Model):
	user 	  	   = models.ForeignKey(UserProfile)
	date 		   = models.DateField()
	date_create    = models.DateTimeField(auto_now=True)

	pp_yprazneniya = models.ForeignKey(PP_Yprazneniya)
	vid_treni      = models.ForeignKey(Vid_Treni)
	vid_podhoda    = models.ForeignKey(Vid_Podhod)

	zanyatie       = models.ForeignKey(Zanyatie)
	status = models.BooleanField(default=True)

	def __unicode__ ( self ) :
		return str(self.id)

#		
class Podhod(models.Model):
	user           = models.ForeignKey(UserProfile)
	date 		   = models.DateField()
	date_create    = models.DateTimeField(auto_now=True)

	zanyatie       = models.ForeignKey(Zanyatie)
	ypraznenie	   = models.ForeignKey(Yprazneniya)
	pp_yprazneniya = models.CharField(max_length=200)
	vid_treni      = models.CharField(max_length=200)
	vid_podhoda    = models.CharField(max_length=200)
	pp_podhoda     = models.CharField(max_length=200)

	povtoreniya    = models.IntegerField(default=0)
	ves            = models.IntegerField(default=0)

	
	status         = models.CharField(max_length=200)



