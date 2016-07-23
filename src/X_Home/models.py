from django.db import models

# Create your models here.

class Articles(models.Model):

	title=models.CharField(max_length=300)
	summary=models.CharField(max_length=300)
	img_url=models.CharField(max_length=300)

