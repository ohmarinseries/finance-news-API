from django.db import models


class ArticleModel(models.Model):
    symbol = models.CharField(max_length=10, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    article_link = models.URLField(null=True)
    publish_date = models.CharField(max_length=50, null=True)


