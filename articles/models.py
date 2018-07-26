from django.db import models


class Article(models.Model):
	 title = models.CharField(max_length=200, unique=True)
	 content = models.TextField()
	 author_name = models.CharField(max_length=200)
	 votes = models.PositiveSmallIntegerField(default=0)