from django.db import models

class Post(models.Model):
 	title = models.CharField(max_length=100)
 	sub_title = models.CharField(max_length=300)
 	content = models.TextField()
