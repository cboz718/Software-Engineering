from django.db import models

class flight(models.Model):
	plane = models.CharField(max_length = 20)
	destination = models.CharField(max_length = 20)
	departure = models.DateTimeField()
	arrival = models.DateTimeField()
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
