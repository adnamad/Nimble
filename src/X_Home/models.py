from django.db import models
# Create your models here.

class Articles(models.Model):

	title=models.CharField(max_length=300)
	summary=models.CharField(max_length=300)
	img_url=models.CharField(max_length=300)
	category = models.CharField(max_length= 20)

class contact(models.Model):
    Email = models.EmailField()
    Name = models.CharField(max_length=20, blank=False)
    Message = models.CharField(max_length=100)

    def __str__(self):
        return  self.Name

