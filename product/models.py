from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        db_table = 'category'

    def __str__(self):
        return f"category: {self.name}"

    def get_absolute_url(self):
        return f"/{self.slug}/"
