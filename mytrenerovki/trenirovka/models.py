# -*- coding: utf-8 -*-
from django.db import models


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

	def __unicode__ ( self ) :
		return self.name

	class Meta :
		verbose_name    = u'Вид упражнения'
		verbose_name_plural  = u'Вид упражнений'
		ordering 		= [u'name']


#		
class Podhod(models.Model):

	user           = models.CharField(max_length=200)

	pp_yprazneniya = models.ForeignKey(PP_Yprazneniya)
	vid_treni      = models.ForeignKey(Vid_Treni)
	vid_podhoda    = models.ForeignKey(Vid_Podhod)
	pp_podhoda     = models.ForeignKey(PP_Podhod)

	povtoreniya = models.IntegerField(default=0)
	ves = models.IntegerField(default=0)

	date = models.DateTimeField('date created')
	status = models.CharField(max_length=200)

