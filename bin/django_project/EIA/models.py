from django.db import connections
from django.db import models

class showid(models.Model):
	eiaplantid = models.IntegerField()
	unit = models.TextField()
	eiaplantname = models.TextField()
	status = models.TextField()
	mwcapacity = models.TextField()
	latitude = models.FloatField()

	class Meta:
		db_table = "eiaplantdata"


