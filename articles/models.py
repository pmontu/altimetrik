from django.db import models


class Article(models.Model):
	 title = models.CharField(max_length=200)
	 content = models.TextField()
	 author_name = models.CharField(max_length=200)