from django.db import models


class GetOrNoneManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class Symbols(models.Model):
    objects = GetOrNoneManager()
    symbol = models.CharField(max_length=10, null=True)


class Article(models.Model):
    objects = GetOrNoneManager()
    symbol = models.ForeignKey('Symbols', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    article_link = models.URLField()
    publish_date = models.CharField(max_length=50)
    external_id = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





